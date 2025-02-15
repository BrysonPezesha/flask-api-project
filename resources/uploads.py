from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.file_service import save_file

uploads_bp = Blueprint('uploads', __name__)

@uploads_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    """Handles file upload (requires authentication)."""
    if 'file' not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    response, status = save_file(file)
    return jsonify(response), status


