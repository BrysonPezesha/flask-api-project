from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from routes import api_bp
from extensions import db  # Import db from extensions
import datetime
import config
import models  # Ensure models are imported so Flask-Migrate detects them
from flask_migrate import Migrate  # Import Flask-Migrate
from celery_app import make_celery

app = Flask(__name__)

app.url_map.strict_slashes = False

# Load configuration
app.config.from_object(config)

# PostgreSQL Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flask_api_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Initialize Flask-Migrate (Handles Migrations)
migrate = Migrate(app, db)

# JWT Configuration
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=15)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta(days=30)

# Initialize JWT after loading config
jwt = JWTManager(app)

# Celery Configuration
app.config.update(
    CELERY_BROKER_URL="redis://localhost:6379/0",
    CELERY_RESULT_BACKEND="redis://localhost:6379/0"
)
celery = make_celery(app)

# Register Blueprint
app.register_blueprint(api_bp, url_prefix='/api')

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Flask API!"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
