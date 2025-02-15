# # In-memory user store (for demo purposes)
# users = {
#     "admin": "password123"
# }

# def verify_user(username, password):
#     """Verifies user credentials."""
#     return username in users and users[username] == password


# # services/auth_service.py (Corrected)
# def verify_user(username, password):
#     # Example authentication logic (replace with your actual user verification)
#     # For testing, you might temporarily hardcode a user:
#     if username == "admin" and password == "secret":
#         return True
#     return False

# services/auth_service.py
def verify_user(username, password):
    """Mock user verification. Replace with real authentication logic."""
    return username == "admin" and password == "password"
