import pika # type: ignore
import json

# RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
channel = connection.channel()

# Declare queue
channel.queue_declare(queue="transactions")

# Publish 10 dummy transaction requests
for _ in range(10):
    channel.basic_publish(exchange="",
                          routing_key="transactions",
                          body=json.dumps({"task": "generate_transaction"}))

print("✅ Sent 10 messages to RabbitMQ queue 'transactions'")
connection.close()
