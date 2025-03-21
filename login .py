# login.py

def login(username, password):
    # Simple login logic (this is just an example)
    stored_username = "user"
    stored_password = "password123"

    if username == stored_username and password == stored_password:
        return "Login successful"
    else:
        return "Invalid username or password"
