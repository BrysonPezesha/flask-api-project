# Creating an entry point for the flask application
# The app won’t show an upload button in the browser since it's an API, but you can test it using:

from flask import Flask, request, jsonify
from routes import app  # Import the app from routes.py

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Flask API!"})

@app.route('/hello/<name>', methods=['GET'])
def greet(name):
    return jsonify({"greeting": f"Hello, {name}!"})

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    return jsonify({"received": data}), 201

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)
