# import os

# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# ALLOWED_EXTENSIONS = {'pdf'}

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def save_file(file):
#     if allowed_file(file.filename):
#         filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#         file.save(filepath)
#         return {"message": "File uploaded successfully", "filename": file.filename}, 201
#     return {"error": "Invalid file type. Only PDFs are allowed."}, 400



import os

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    """Checks if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file):
    """Saves an uploaded file if it meets criteria."""
    if allowed_file(file.filename):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return {"message": "File uploaded successfully", "filename": file.filename}, 201
    return {"error": "Invalid file type. Only PDFs are allowed."}, 400


