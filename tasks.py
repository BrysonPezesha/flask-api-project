from celery import Celery
from celery.schedules import crontab  # For periodic tasks
from faker import Faker  # type: ignore
import psycopg2
import json
import os
import pika  # type: ignore
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize Celery
celery_app = Celery("tasks")
celery_app.config_from_object({
    "broker_url": "pyamqp://guest:guest@rabbitmq:5672//",
    "result_backend": "redis://redis:6379/0",
    "task_serializer": "json",
    "accept_content": ["json"],
    "timezone": "Africa/Nairobi",
})

# Database connection parameters
DB_PARAMS = {
    "dbname": "flask_api_db",
    "user": "postgres",
    "password": "postgres",
    "host": "postgres",
    "port": "5432"
}

# Fake data generator
faker = Faker()

@celery_app.task
def generate_transaction():
    """Generate a dummy Mpesa-like transaction and insert into PostgreSQL."""
    transaction = {
        "transaction_id": faker.uuid4(),
        "amount": round(faker.random_number(digits=4), 2),
        "currency": "KES",
        "timestamp": faker.date_time_this_year().isoformat(),
        "sender": faker.phone_number(),
        "receiver": faker.phone_number(),
        "status": faker.random_element(["Completed", "Pending", "Failed"])
    }

    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO transactions (transaction_id, amount, currency, timestamp, sender, receiver, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (transaction["transaction_id"], transaction["amount"], transaction["currency"],
             transaction["timestamp"], transaction["sender"], transaction["receiver"], transaction["status"])
        )
        conn.commit()
        cur.close()
        conn.close()
        logging.info(f"✅ Transaction {transaction['transaction_id']} inserted successfully.")
        return f"Transaction {transaction['transaction_id']} inserted successfully."
    except Exception as e:
        logging.error(f"❌ Error inserting transaction: {str(e)}")
        return str(e)

def consume_messages():
    """Consumes messages from RabbitMQ and triggers Celery tasks."""
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
        channel = connection.channel()
        channel.queue_declare(queue="transactions")

        def callback(ch, method, properties, body):
            """Trigger Celery task when a message arrives."""
            message = json.loads(body)
            if message["task"] == "generate_transaction":
                result = generate_transaction.delay()
                logging.info(f"✅ Task sent to Celery: {result.id}")

        channel.basic_consume(queue="transactions", on_message_callback=callback, auto_ack=True)
        logging.info("🟢 Waiting for messages...")
        channel.start_consuming()
    except Exception as e:
        logging.error(f"❌ RabbitMQ connection failed: {str(e)}")

# Periodic Task - Generate transaction every 30 seconds
celery_app.conf.beat_schedule = {
    "generate_transaction_every_30_secs": {
        "task": "tasks.generate_transaction",
        "schedule": 10.0,  # Run every 10 seconds
    },
}

if __name__ == "__main__":
    consume_messages()

