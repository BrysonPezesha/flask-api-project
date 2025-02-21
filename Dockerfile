# Use an official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install faker
RUN pip install pika

# Copy the entire project
COPY . .

# Command to run Celery
CMD ["celery", "-A", "celery_app", "worker", "--loglevel=info"]
