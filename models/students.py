from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest
from database import Database
import mysql.connector
import json

students_bp = Blueprint('students', __name__)

@students_bp.route('/add_student', methods=['POST'])
def add_student():
    data = request.json
    studentid = data.get('studentid')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    birthdate = data.get('birthdate')
    classid = data.get('classid')

    if not studentid or not firstname or not lastname or not birthdate or not classid:
        return jsonify({'error': 'All fields (studentid, firstname, lastname, birthdate, classid) are required'}), 400

    try:
        db = Database()
        #query = "INSERT INTO students (studentid, firstname, lastname, birthdate, classid) VALUES (%s, %s, %s, %s, %s);"
        #args = (studentid, firstname, lastname, birthdate, classid)
        #db.execute_query(query, args)

        # Call stored procedure to add a student
        query = "registerstudent" #"CALL `parent-student  Tracking`.`registerstudent`(%s, %s, %s, %s, %s);"
        args = (studentid, firstname, lastname, birthdate, classid)
        db.execute_query(query, args)  # Set multi to False for single query

        print("Student added successfully")

        return jsonify({'message': 'Student added successfully'}), 201

    except Exception as e:
        print("Error:", e)
        # Log the error or return a proper error response
        return jsonify({'error': 'An error occurred'}), 500

@students_bp.route('/get_students', methods=['GET'])
def get_students():
    try:
        # Create a database connection
        db = Database()

        # Call stored procedure to get all students
        query = "students"


        students = db.get_data(query, multi=True)
        # Check if students is None or empty
        if students is None or not students:
            return jsonify([]), 200  # Return an empty list if no students found

        # Create a list of dictionaries containing student information
        student_list = []
        for student in students:
            student_info = {
                'studentid': student[0],
                'firstname': student[1],
                'lastname': student[2],
                'birthdate': student[3],
                'classid': student[4],
                'createdat': student[5],
                'updatedat': student[6]
            }
            student_list.append(student_info)

        # Return the list of student information as JSON response
        #return jsonify(student_list), 200
        return render_template("students.html",students = student_list)

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'An error occurred'}), 500


@students_bp.route('/delete_student/<int:studentid>', methods=['POST'])
def delete_student(studentid):
    # Call stored procedure to delete a student
    query = "deletestudent"
    args = (studentid,)
    db = Database()
    db.execute_query(query,args)

    print("Student deleted successfully from database")

    return jsonify({'message': 'Student deleted successfully'}), 200
