# Flask API Project

## Overview
This is a Flask-based API that supports authentication, file uploads, and protected endpoints. The project follows a structured approach using Blueprints for modularity.

## Features
- JWT Authentication (Flask-JWT-Extended)
- File Upload API
- Protected Routes
- Structured project layout

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd flask-api-project
```

### 2. Create a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file and configure necessary variables:
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
```

### 5. Run the Flask Server
```sh
flask run --host=0.0.0.0 --port=5001
```

## API Endpoints

### Authentication
#### Login (Get Access Token)
```sh
POST /auth/login
```
- Request Body:
```json
{
  "username": "admin",
  "password": "password"
}
```
- Response:
```json
{
  "access_token": "<JWT_TOKEN>",
  "refresh_token": "<JWT_REFRESH_TOKEN>"
}
```

### Protected Route
```sh
GET /protected/
```
- Requires `Authorization: Bearer <ACCESS_TOKEN>`

### File Upload
```sh
POST /files/upload
```
- Requires `Authorization: Bearer <ACCESS_TOKEN>`
- Request Form Data:
  - `file`: The file to upload

## Common Issues & Troubleshooting

### 1. Flask Command Not Found
Ensure you are inside the virtual environment:
```sh
source venv/bin/activate
```

### 2. Token Expired
If you receive `"Token has expired"`, generate a new access token using the refresh token:
```sh
POST /auth/refresh
```

### 3. 404 Not Found
- Ensure the Flask server is running (`flask run`)
- Verify the correct port (default: `5001`)
- Check if the blueprint is registered in `app.py`

## Future Enhancements
- Database integration (PostgreSQL, MongoDB)
- Docker setup for deployment
- Logging & monitoring

