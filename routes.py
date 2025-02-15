# from flask import Blueprint
# from resources.auth import auth_bp
# from resources.protected import protected_bp

# api_bp = Blueprint('api', __name__)

# # Register Blueprints
# api_bp.register_blueprint(auth_bp)
# api_bp.register_blueprint(protected_bp)


# from flask import Blueprint, request, jsonify
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity # type: ignore
# import os
# from flask import Flask
# from flask_jwt_extended import JWTManager # type: ignore
# from routes import api_bp  # Import routes

# app = Flask(__name__)

# # Configure JWT
# app.config['JWT_SECRET_KEY'] = 'super-secret-key' 

# api_bp = Blueprint('api', __name__)  

# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# ALLOWED_EXTENSIONS = {'pdf'}

# # Dummy users database
# users = {"admin": "password123"}

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # Home route
# @api_bp.route('/', methods=['GET'])
# def home():
#     return jsonify({"message": "Welcome to my Flask API!"}), 200

# # Login route (Generates JWT)
# @api_bp.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')

#     if username in users and users[username] == password:
#         access_token = create_access_token(identity=username)
#         return jsonify({"access_token": access_token}), 200

#     return jsonify({"error": "Invalid credentials"}), 401

# # Protected route (Requires JWT)
# @api_bp.route('/protected', methods=['GET'])
# @jwt_required()
# def protected():
#     current_user = get_jwt_identity()
#     return jsonify({"message": f"Hello, {current_user}! This is a protected route."}), 200

# # File upload route (Requires JWT)
# @api_bp.route('/files/upload', methods=['POST'])
# @jwt_required()
# def upload_file():
#     """Handles file upload (requires authentication)."""
#     if 'file' not in request.files:
#         return jsonify({"error": "No file part in request"}), 400

#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({"error": "No file selected"}), 400

#     if allowed_file(file.filename):
#         filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#         file.save(filepath)
#         return jsonify({
#             "message": "File uploaded successfully",
#             "filename": file.filename
#         }), 201

#     return jsonify({"error": "Invalid file type. Only PDFs are allowed."}), 400

# # Change this in production
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=15)  # Access token expiry
# app.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta(days=30)  # Refresh token expiry
# jwt = JWTManager(app)

# # Register Blueprint
# app.register_blueprint(api_bp)




from flask import Blueprint, jsonify
from resources.auth import auth_bp
from resources.protected import protected_bp
from resources.uploads import uploads_bp

api_bp = Blueprint('api', __name__)

# Root API Route (Fixes 404 for /api/)
@api_bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "API is working!"}), 200

# Register Sub-Blueprints
api_bp.register_blueprint(auth_bp, url_prefix="/auth")
api_bp.register_blueprint(protected_bp, url_prefix="/protected")
api_bp.register_blueprint(uploads_bp, url_prefix="/files")





