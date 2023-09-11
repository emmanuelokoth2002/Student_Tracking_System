from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest
from database import Database

asignments_bp = Blueprint('assignments', __name__)

@asignments_bp.route('/add_assignment', methods=['POST'])
def add_assignment():
    data = request.json
    assignmentid = data.get('assignmentid')
    classid = data.get('classid')
    title = data.get('title')
    description = data.get('description')
    duedate = data.get('duedate')

    if not assignmentid or not classid or not title or not description or not duedate:
        raise BadRequest('All fields (assignmentid, classid, title, description, duedate) are required.')
    
    db = Database()
    # Call stored procedure to add a assignments using parameterized query
    query = "addupdateassignment"
    values = (assignmentid, classid, title, description, duedate)
    
    db.execute_query(query, values, multi=True)

    return jsonify({'message': 'Assignment added successfully'}), 201

@asignments_bp.route('/get_assignments', methods=['GET'])
def get_assignments():
    try:
        # Create a database connection
        db = Database()

        # Call stored procedure to get all assignments
        query = "assignments"

        assignments = db.get_data(query, multi=True)

        print("Retrieved assignments:", assignments)

        # Create a list of dictionaries containing assignments information
        assignment_list = []
        for assignment in assignments:
            assignment_info = {
                'assignmentid': assignment[0],
                'classid': assignment[1],
                'title': assignment[2],
                'description': assignment[3],
                'duedate': assignment[4],
                'createdat': assignment[5],
                'updatedat': assignment[6]
            }
            assignment_list.append(assignment_info)

        # Return the list of assignments information as JSON response
        #return jsonify(assignment_list), 200
        return render_template('assignment.html',assignments = assignment_list)

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'An error occurred'}), 500


@asignments_bp.route('/delete_assignment/<int:assignmentid>', methods=['POST'])
def delete_parent(assignmentid):
    # Call stored procedure to delete a assignments
    query = "deleteassignment"
    args = (assignmentid,)
    db = Database()
    db.execute_query(query,args)

    return jsonify({'message': 'Asignment deleted successfully'}), 200