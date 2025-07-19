from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from db import mongo

auth_bp = Blueprint('auth', __name__)

# User Signup
@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"msg": "Username and Password are required"}), 400
    
    # Check if user exists
    existing_user = mongo.db.users.find_one({"username": username})
    if existing_user:
        return jsonify({"msg": "User already exists"}), 400
    
    # Hash the password
    hashed_password = generate_password_hash(password)
    
    # Insert new user into MongoDB
    mongo.db.users.insert_one({
        "username": username,
        "password": hashed_password
    })
    
    return jsonify({"msg": "User created successfully!"}), 201


# User Login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"msg": "Username and Password are required"}), 400
    
    user = mongo.db.users.find_one({"username": username})
    
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"msg": "Invalid username or password"}), 401
    
    # Create JWT token
    access_token = create_access_token(identity=username)
    
    return jsonify({"msg": "Login successful", "access_token": access_token}), 200
