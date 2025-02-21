from app import app, db
from models.user import User  # Ensure your User model is correctly imported

def test_crud():
    with app.app_context():
        # Check if the user already exists
        user = User.query.filter_by(username="testuser").first()
        
        if user:
            print(f"User '{user.username}' already exists with ID: {user.id}")
            
            # Option 1: Update the user
            user.email = "updatedemail@example.com"
            db.session.commit()
            print(f"Updated email for {user.username} to {user.email}")
            
            # Option 2: Delete and recreate the user (Uncomment if needed)
            # db.session.delete(user)
            # db.session.commit()
            # print("User deleted!")
        else:
            # Create a new user if not found
            new_user = User(username="testuser", email="test@example.com", password_hash="testhash")
            db.session.add(new_user)
            db.session.commit()
            print(f"New user created with ID: {new_user.id}")
        
        # List all users
        users = User.query.all()
        print("\nAll Users:")
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

if __name__ == "__main__":
    test_crud()
