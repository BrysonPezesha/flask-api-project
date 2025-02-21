from flask import Blueprint, jsonify
from .auth import auth_bp         # Authentication endpoints (login/register)
from .protected import protected_bp  # Protected endpoints (if any)
from .users import users_bp       # Users CRUD endpoints
from .uploads import uploads_bp   # Uploads CRUD endpoints


api_bp = Blueprint('api', __name__)

@api_bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "API is working!"}), 200

# Register Blueprints with URL prefixes
api_bp.register_blueprint(auth_bp, url_prefix="/auth")
api_bp.register_blueprint(protected_bp, url_prefix="/protected")
api_bp.register_blueprint(users_bp, url_prefix="/users")
api_bp.register_blueprint(uploads_bp, url_prefix="/uploads")
