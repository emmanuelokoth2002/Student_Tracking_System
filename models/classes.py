from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest
from database import Database

classes_bp = Blueprint('classes', __name__)

@classes_bp.route('/add_class', methods=['POST'])
def add_class():
    data = request.json
    classid = data.get('classid')
    classname = data.get('classname')
    teacherid = data.get('teacherid')
    startdate = data.get('startdate')
    enddate = data.get('enddate')

    if not classid or not classname or not teacherid or not startdate or not enddate:
        raise BadRequest('All fields (classid, classname, teacherid, startdate, enddate) are required.')
    
    db = Database()
    # Call stored procedure to add a classes using parameterized query
    query = "registeclass"
    values = (classid, classname, teacherid, startdate, enddate)
    
    db.execute_query(query, values, multi=True)

    return jsonify({'message': 'Class added successfully'}), 201

@classes_bp.route('/get_classes', methods=['GET'])
def get_classes():
    try:
        # Create a database connection
        db = Database()

        # Call stored procedure to get all classes
        query = "classes"

        classes = db.get_data(query, multi=True)

        print("Retrieved classes:", classes)

        # Create a list of dictionaries containing classes information
        class_list = []
        for classes in classes:
            class_info = {
                'classid': classes[0],
                'classname': classes[1],
                'teacherid': classes[2],
                'startdate': classes[3],
                'enddate': classes[4],
                'createdat': classes[5],
                'updatedat': classes[6]
            }
            class_list.append(class_info)

        # Return the list of classes information as JSON response
        #return jsonify(class_list), 200
        return render_template("classes.html",classes = class_list)

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'An error occurred'}), 500


@classes_bp.route('/delete_class/<int:classid>', methods=['POST'])
def delete_parent(classid):
    # Call stored procedure to delete a classes
    query = "deleteclass"
    args = (classid,)
    db = Database()
    db.execute_query(query,args)

    return jsonify({'message': 'Class deleted successfully'}), 200
