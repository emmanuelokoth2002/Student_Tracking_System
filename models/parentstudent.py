from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest
from database import Database

relation_bp = Blueprint('relations', __name__)

@relation_bp.route('/add_relation', methods=['POST'])
def add_relation():
    data = request.json
    parentid = data.get('parentid')
    studentid = data.get('studentid')

    if not parentid or not studentid:
        raise BadRequest('All fields (parentid, studentid) are required.')
    
    db = Database()
    # Call stored procedure to add a relation using parameterized query
    query = "addupadatepatent-student"
    values = (parentid, studentid)
    
    db.execute_query(query, values, multi=True)

    return jsonify({'message': 'Parent Student relation added successfully'}), 201

@relation_bp.route('/get_relation', methods=['GET'])
def get_relation():
    try:
        # Create a database connection
        db = Database()

        # Call stored procedure to get all relations
        query = "relation-student"

        relations = db.get_data(query, multi=True)

        print("Retrieved relations:", relations)

        # Create a list of dictionaries containing relation information
        relation_list = []
        for relation in relations:
            relation_info = {
                'parentid': relation[0],
                'studentid': relation[1],
                'createdat': relation[2],
                'updatedat': relation[3]
            }
            relation_list.append(relation_info)

        # Return the list of relation information as JSON response
        #return jsonify(relation_list), 200
        return render_template('parentstudent.html',relation = relation_list)

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'An error occurred'}), 500
