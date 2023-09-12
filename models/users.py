from flask import Blueprint, redirect, render_template, request, jsonify, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from database import Database

users_bp = Blueprint('users', __name__)
db = Database()

@users_bp.route('/')
def index():
    return render_template("index.html")

@users_bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    userid = data.get('userid')
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if not userid or not username or not password:
        return jsonify({'message': 'Userid Username and password are required'}), 400

    # Check if the username already exists
    query_check_username = "SELECT * FROM users WHERE username = %s"
    args_check_username = (username,)
    existing_user = db.get_data(query_check_username, args_check_username)

    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    # Insert the new user into the database
    password_hash = generate_password_hash(password)
    query_insert_user = "INSERT INTO users (userid, username, password_hash, role) VALUES (%s, %s, %s, %s)"
    args_insert_user = (userid, username, password_hash, role)
    
    try:
        db.connect()
        db.execute_query(query_insert_user, args_insert_user)
        db.close_connection()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'An error occurred while registering the user'}), 500

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400

        # Retrieve the user from the database
        query_select_user = "SELECT * FROM users WHERE username = %s"
        args_select_user = (username,)
        user = db.get_data(query_select_user, args_select_user)

        if not user or not check_password_hash(user[0]['password_hash'], password):
            return jsonify({'message': 'Invalid credentials'}), 401

        # Redirect to the 'dashboard' route upon successful login
        return redirect(url_for('users.dashboard'))

    # Render the 'login.html' file for GET requests
    return render_template("login.html")

@users_bp.route('/dashboard')
def dashboard():
    # Render the 'dashboard.html' file for the logged-in user
    return render_template("dashboard.html")

