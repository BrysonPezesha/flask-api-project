from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from routes import api_bp
import datetime  

app = Flask(__name__)

# JWT Configuration (Change for production)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=15)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta(days=30)

jwt = JWTManager(app)

# Register Blueprint
app.register_blueprint(api_bp, url_prefix='/api')  # All routes start with /api

# ✅ Add Root Route (Fixes 404 for "/")
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Flask API!"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)









