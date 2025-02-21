import os

DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "127.0.0.1"  # or "localhost"
DB_PORT = "5432"  # Only the port number
DB_NAME = "flask_api_db"

SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
