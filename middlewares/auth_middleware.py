
from models.User import User
from functools import wraps
from flask import redirect, request,  session, url_for
def is_authenticated(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user_id = session.get('user_id')
        # Attempt to fetch the user from the database
        current_user = get_user(user_id)
        # Check if the user exists in the database
        if not current_user:
            return redirect_to_signin()
        return f( *args, **kwargs)
    return decorated

def get_user( user_id):
    try:
        # Perform the database query to retrieve the user
        user = User.query.get(user_id)
        return user
    except Exception as e:
        # Handle database query errors gracefully
        print(f"Error fetching user from database: {e}")
        return None

def redirect_to_signin( ):
    return redirect(url_for('signin'))