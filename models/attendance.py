from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest
from database import Database

attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/add_attendance', methods=['POST'])
def add_attendance():
    data = request.json
    attendanceid = data.get('attendanceid')
    studentid = data.get('studentid')
    classid = data.get('classid')
    attendancedate = data.get('attendancedate')
    status = data.get('status')

    if not attendanceid or not studentid or not classid or not attendancedate or not status:
        raise BadRequest('All fields (attendanceid, studentid, classid, attendancedate, status) are required.')
    
    db = Database()
    # Call stored procedure to add a attend using parameterized query
    query = "addupdateattendance"
    values = (attendanceid, studentid, classid, attendancedate, status)
    
    db.execute_query(query, values, multi=True)

    return jsonify({'message': 'Attendance added successfully'}), 201

@attendance_bp.route('/get_attendance', methods=['GET'])
def get_attendance():
    try:
        # Create a database connection
        db = Database()

        # Call stored procedure to get all attendance
        query = "attendance"

        attendance = db.get_data(query, multi=True)

        print("Retrieved attendance:", attendance)

        # Create a list of dictionaries containing attend information
        attendance_list = []
        for attend in attendance:
            attend_info = {
                'attendanceid': attend[0],
                'studentid': attend[1],
                'classid': attend[2],
                'attendancedate': attend[3],
                'status': attend[4],
                'createdat': attend[5],
                'updatedat': attend[6]
            }
            attendance_list.append(attend_info)

        # Return the list of attend information as JSON response
        #return jsonify(attendance_list), 200
        return render_template('attendance.html',attendance = attendance_list)

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'An error occurred'}), 500


@attendance_bp.route('/delete_attend/<int:attendanceid>', methods=['POST'])
def delete_attend(attendanceid):
    # Call stored procedure to delete a attend
    query = "deleteattendance"
    args = (attendanceid,)
    db = Database()
    db.execute_query(query,args)

    return jsonify({'message': 'attend deleted successfully'}), 200
