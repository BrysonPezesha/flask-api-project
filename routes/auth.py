from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User
from flask_jwt_extended import create_access_token
from services.user_service import create_user, get_user_by_email

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or not all(k in data for k in ["username", "email", "password"]):
        return jsonify({"error": "Missing fields"}), 400

    if get_user_by_email(data["email"]):
        return jsonify({"error": "User already exists"}), 400

    user = create_user(data["username"], data["email"], data["password"])
    return jsonify({"message": "User registered", "user_id": user.id}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = get_user_by_email(data["email"])
    if not user or not user.check_password(data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), 200
