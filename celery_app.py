from celery import Celery

def make_celery(app_name=__name__):
    return Celery(
        app_name,
        broker="pyamqp://guest:guest@rabbitmq:5672//",  # Use service name in Docker
        backend="redis://redis:6379/0"
    )

celery = make_celery()


@celery.task(name="celery_app.add")  # Explicitly set the name
def add(x, y):
    return x + y

from celery_app import add