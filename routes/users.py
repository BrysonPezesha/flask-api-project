from flask import Blueprint, request, jsonify
from models.user import User
from extensions import db

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
def get_users():
    """Retrieve all users."""
    users = User.query.all()
    result = [
        {"id": user.id, "username": user.username, "email": user.email}
        for user in users
    ]
    return jsonify(result), 200

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a single user by ID."""
    user = User.query.get(user_id)
    if user:
        return jsonify({"id": user.id, "username": user.username, "email": user.email}), 200
    return jsonify({"error": "User not found"}), 404

@users_bp.route('/', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    
    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    # Check if user already exists
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({"error": "User already exists"}), 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created", "user_id": new_user.id}), 201

@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)
    if "password" in data:
        user.set_password(data["password"])
    db.session.commit()
    return jsonify({"message": "User updated"}), 200

@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete an existing user."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200
