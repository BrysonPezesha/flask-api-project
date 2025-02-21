# # In-memory user store (for demo purposes)
# users = {
#     "admin": "password123"
# }

# def verify_user(username, password):
#     """Verifies user credentials."""
#     return username in users and users[username] == password


# services/auth_service.py
def verify_user(username, password):
    """Mock user verification. Replace with real authentication logic."""
    return username == "admin" and password == "password"
