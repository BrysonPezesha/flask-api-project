# from flask import Blueprint, jsonify
# from flask_jwt_extended import jwt_required, get_jwt_identity # type: ignore

# protected_bp = Blueprint('protected', __name__)

# @protected_bp.route('/', methods=['GET'])
# @jwt_required()
# def protected():
#     """A protected endpoint that requires authentication."""
#     current_user = get_jwt_identity()
#     return jsonify(message=f"Hello, {current_user}! This is a protected route."), 200


from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

protected_bp = Blueprint('protected', __name__)

@protected_bp.route('/', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(message=f"Hello, {current_user}! This is a protected route."), 200

