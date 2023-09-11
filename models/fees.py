from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest
from database import Database

fees_bp = Blueprint('fees', __name__)

@fees_bp.route('/add_fee', methods=['POST'])
def add_fee():
    data = request.json
    feesid = data.get('feesid')
    studentid = data.get('studentid ')
    amount = data.get('amount')
    duedate = data.get('duedate')
    status = data.get('status')

    if not feesid or not studentid or not amount or not duedate or not status:
        raise BadRequest('All fields (feesid, studentid , amount, duedate, status) are required.')
    
    db = Database()
    # Call stored procedure to add a fee using parameterized query
    query = "addupdatefees"
    values = (feesid, studentid , amount, duedate, status)
    
    db.execute_query(query, values, multi=True)

    return jsonify({'message': 'Parent added successfully'}), 201

@fees_bp.route('/get_fees', methods=['GET'])
def get_fees():
    try:
        # Create a database connection
        db = Database()

        # Call stored procedure to get all fees
        query = "fees"

        fees = db.get_data(query, multi=True)

        print("Retrieved fees:", fees)

        # Create a list of dictionaries containing fee information
        fees_list = []
        for fee in fees:
            fee_info = {
                'feesid': fee[0],
                'studentid ': fee[1],
                'amount': fee[2],
                'duedate': fee[3],
                'status': fee[4],
                'createdat': fee[5],
                'updatedat': fee[6]
            }
            fees_list.append(fee_info)

        # Return the list of fee information as JSON response
        #return jsonify(fees_list), 200
        return render_template('fees.html',fees = fees_list)

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'An error occurred'}), 500


@fees_bp.route('/delete_fee/<int:feesid>', methods=['POST'])
def delete_fee(feesid):
    # Call stored procedure to delete a fee
    query = "deletefees"
    args = (feesid,)
    db = Database()
    db.execute_query(query,args)

    return jsonify({'message': 'Fee deleted successfully'}), 200
