from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({"message": "Unauthorized. Please login.", "error": str(e)}), 401
    return decorated

def get_current_user_id():
    """Helper to get logged-in user's ID from JWT token"""
    try:
        return get_jwt_identity()
    except:
        return None
