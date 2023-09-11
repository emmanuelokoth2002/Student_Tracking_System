from flask import Blueprint, render_template, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from database import Database

users_bp = Blueprint('users', __name__)
db = Database()

@users_bp.route('/')
def index():
    #return "<h1>Hello, World!</h1>"
    return render_template("index.html")

@users_bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    userid = data['userid']
    username = data['username']
    password_hash = data['password_hash']
    role = data['role']

    # Check if the username already exists
    query_check_username = "CheckUser"
    args_check_username = (userid,username,password_hash)
    existing_user = db.get_data(query_check_username, args_check_username)

    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    # Insert the new user into the database
    password_hash = generate_password_hash(password_hash)
    query_insert_user = "registeruser"
    args_insert_user = (userid,username, password_hash, role)
    
    try:
        db.connect()
        db.execute_query(query_insert_user, args_insert_user)
        db.close_connection()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'An error occurred while registering the user'}), 500

@users_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password_hash']

    # Retrieve the user from the database
    query_select_user = "users"
    args_select_user = (username,)
    user = db.get_data(query_select_user, args_select_user)

    if not user or not check_password_hash(user[0]['password_hash'], password):
        return jsonify({'message': 'Invalid credentials'}), 401

    return jsonify({'message': 'Login successful'}), 200