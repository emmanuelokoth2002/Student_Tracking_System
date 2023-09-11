from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
from database import Database

notifications.bp = Blueprint('notifications', __name__)

@notifications.bp.route('/add_notification', methods=['POST'])
def add_notification():
    data = request.json
    parentid = data.get('parentid')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    email = data.get('email')
    phonenumber = data.get('phonenumber')

    if not parentid or not firstname or not lastname or not email or not phonenumber:
        raise BadRequest('All fields (parentid, firstname, lastname, email, phonenumber) are required.')
    
    db = Database()
    # Call stored procedure to add a parent using parameterized query
    query = "registerparent"
    values = (parentid, firstname, lastname, email, phonenumber)
    
    db.execute_query(query, values, multi=True)

    return jsonify({'message': 'Parent added successfully'}), 201

@notifications.bp.route('/get_notifications', methods=['GET'])
def get_notifications():
    try:
        # Create a database connection
        db = Database()

        # Call stored procedure to get all notifications
        query = "notifications"

        notifications = db.get_data(query, multi=True)

        print("Retrieved notifications:", notifications)

        # Create a list of dictionaries containing parent information
        parent_list = []
        for parent in notifications:
            parent_info = {
                'parentid': parent[0],
                'firstname': parent[1],
                'lastname': parent[2],
                'email': parent[3],
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


@notifications.bp.route('/delete_parent/<int:parentid>', methods=['POST'])
def delete_parent(parentid):
    # Call stored procedure to delete a parent
    query = "deleteparent"
    args = (parentid,)
    db = Database()
    db.execute_query(query,args)

    return jsonify({'message': 'Parent deleted successfully'}), 200