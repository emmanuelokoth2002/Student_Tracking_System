from http.client import BAD_REQUEST
from flask import Blueprint, render_template, request, jsonify
from database import Database

teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('/add_teacher', methods=['POST'])
def add_teacher():
    data = request.json
    teacherid = data.get('teacherid')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    email = data.get('email')
    phonenumber = data.get('phonenumber')

    if not teacherid or not firstname or not lastname or not email or not phonenumber:
        raise BAD_REQUEST('All fields (teacherid, firstname, lastname, email, phonenumber) are required.')
    
    db = Database()
    # Call stored procedure to add a parent using parameterized query
    query = "registerteacher"
    values = (teacherid, firstname, lastname, email, phonenumber)
    
    db.execute_query(query, values, multi=True)

    return jsonify({'message': 'Teacher added successfully'}), 201

@teachers_bp.route('/get_teachers', methods=['GET'])
def get_teachers():
    try:
        # Create a database connection
        db = Database()

        # Call the stored procedure to get all teachers
        query = "teachers"  # Use the name of your stored procedure

        teachers = db.get_data(query, multi=True)

        # Check if teachers is None or empty
        if teachers is None or not teachers:
            return jsonify([]), 200  # Return an empty list if no teachers found

        # Create a list of dictionaries containing teacher information
        teacher_list = []
        for teacher in teachers:
            teacher_info = {
                'teacher_id': teacher[0],
                'first_name': teacher[1],
                'last_name': teacher[2],
                'email': teacher[3],
                'phonenumber':teacher[4],
                'createdat':teacher[5],
                'updatedat':teacher[6]
                # Add other fields as needed
            }
            teacher_list.append(teacher_info)

        # Return the list of teacher information as a JSON response
        #return jsonify(teacher_list), 200
        return render_template("teachers.html",teachers = teacher_list)

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'An error occurred'}), 500
    
@teachers_bp.route('/delete_teacher/<int:teacherid>', methods=['POST'])
def delete_teacher(teacherid):
    # Call stored procedure to delete a parent
    query = "deleteteacher"
    args = (teacherid,)
    db = Database()
    db.execute_query(query,args)

    return jsonify({'message': 'Teacher deleted successfully'}), 200

