# Creating an entry point for the flask application
# The app won’t show an upload button in the browser since it's an API, but you can test it using:

from flask import Flask
from routes import app  # Import the app from routes.py

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the LLM-Powered Bank Statement Extraction API!"

if __name__ == '__main__':
    app.run(debug=True)