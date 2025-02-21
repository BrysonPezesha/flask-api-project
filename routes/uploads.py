from flask import Blueprint, request, jsonify
from models.upload import Upload
from extensions import db


uploads_bp = Blueprint('file_uploads', __name__)


@uploads_bp.route('/', methods=['GET'])
def get_uploads():
    """Retrieve all uploads."""
    uploads = Upload.query.all()
    result = [
        {
            "id": upload.id,
            "filename": upload.filename,
            "uploaded_at": upload.uploaded_at.isoformat() if upload.uploaded_at else None
        }
        for upload in uploads
    ]
    return jsonify(result), 200

@uploads_bp.route('/<int:upload_id>', methods=['GET'])
def get_upload(upload_id):
    """Retrieve a single upload by ID."""
    upload = Upload.query.get(upload_id)
    if upload:
        return jsonify({
            "id": upload.id,
            "filename": upload.filename,
            "uploaded_at": upload.uploaded_at.isoformat() if upload.uploaded_at else None
        }), 200
    return jsonify({"error": "Upload not found"}), 404

@uploads_bp.route('/', methods=['POST'])
def create_upload():
    """Create a new upload record (metadata only)."""
    data = request.get_json()
    filename = data.get("filename")
    if not filename:
        return jsonify({"error": "Missing filename"}), 400

    new_upload = Upload(filename=filename)
    db.session.add(new_upload)
    db.session.commit()
    return jsonify({"message": "Upload created", "upload_id": new_upload.id}), 201

@uploads_bp.route('/<int:upload_id>', methods=['PUT'])
def update_upload(upload_id):
    """Update an existing upload record."""
    upload = Upload.query.get(upload_id)
    if not upload:
        return jsonify({"error": "Upload not found"}), 404

    data = request.get_json()
    upload.filename = data.get("filename", upload.filename)
    db.session.commit()
    return jsonify({"message": "Upload updated"}), 200

@uploads_bp.route('/<int:upload_id>', methods=['DELETE'])
def delete_upload(upload_id):
    """Delete an upload record."""
    upload = Upload.query.get(upload_id)
    if not upload:
        return jsonify({"error": "Upload not found"}), 404

    db.session.delete(upload)
    db.session.commit()
    return jsonify({"message": "Upload deleted"}), 200
