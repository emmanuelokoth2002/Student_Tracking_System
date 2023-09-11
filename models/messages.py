from pyexpat.errors import messages
from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
from database import Database

messages.bp = Blueprint('parents', __name__)

@messages.bp.route('/add_message', methods=['POST'])
def add_message():
    data = request.json
    messageid = data.get('messageid')
    senderid = data.get('senderid')
    receiverid = data.get('receiverid')
    messagecontent = data.get('messagecontent')

    if not messageid or not senderid or not receiverid or not messagecontent:
        raise BadRequest('All fields (messageid, senderid, receiverid, messagecontent) are required.')
    
    db = Database()
    # Call stored procedure to add a parent using parameterized query
    query = "createupdatemessage"
    values = (messageid, senderid, receiverid, messagecontent)
    
    db.execute_query(query, values, multi=True)

    return jsonify({'message': 'Message added successfully'}), 201

@messages.bp.route('/get_messages', methods=['GET'])
def get_messages():
    try:
        # Create a database connection
        db = Database()

        # Call stored procedure to get all parents
        query = "messages"

        parents = db.get_data(query, multi=True)

        print("Retrieved parents:", parents)

        # Create a list of dictionaries containing parent information
        parent_list = []
        for parent in parents:
            parent_info = {
                'messageid': parent[0],
                'senderid': parent[1],
                'receiverid': parent[2],
                'messagecontent': parent[3],
                'phonenumber': parent[4],
                'createdat': parent[5],
                'updatedat': parent[6]
            }
            parent_list.append(parent_info)

        # Return the list of parent information as JSON response
        return jsonify(parent_list), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'An error occurred'}), 500


@messages.bp.route('/delete_parent/<int:messageid>', methods=['POST'])
def delete_parent(messageid):
    # Call stored procedure to delete a parent
    query = "deleteparent"
    args = (messageid,)
    db = Database()
    db.execute_query(query,args)

    return jsonify({'message': 'Parent deleted successfully'}), 200