# from flask import Blueprint, request, jsonify
# from flask_jwt_extended import create_access_token, create_refresh_token
# from services.auth_service import verify_user

# auth_bp = Blueprint('auth', __name__)

# @auth_bp.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get("username")
#     password = data.get("password")
    
#     if verify_user(username, password):
#         access_token = create_access_token(identity=username)
#         refresh_token = create_refresh_token(identity=username)
#         return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    
#     return jsonify({"error": "Invalid credentials"}), 401


from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from services.auth_service import verify_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if verify_user(username, password):
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    
    return jsonify({"error": "Invalid credentials"}), 401
