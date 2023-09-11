from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest
from database import Database

news_bp = Blueprint('news', __name__)

@news_bp.route('/add_news', methods=['POST'])
def add_news():
    data = request.json
    newsid = data.get('newsid')
    content = data.get('content')
    publishdate = data.get('publishdate')

    if not newsid or not content or not publishdate:
        raise BadRequest('All fields (newsid, content, publishdate) are required.')
    
    db = Database()
    # Call stored procedure to add a new using parameterized query
    query = "addupdatenews"
    values = (newsid, content, publishdate)
    
    db.execute_query(query, values, multi=True)

    return jsonify({'message': 'News added successfully'}), 201

@news_bp.route('/get_news', methods=['GET'])
def get_news():
    try:
        # Create a database connection
        db = Database()

        # Call stored procedure to get all news
        query = "news"

        news = db.get_data(query, multi=True)

        print("Retrieved news:", news)

        # Create a list of dictionaries containing new information
        news_list = []
        for new in news:
            new_info = {
                'newsid': new[0],
                'content': new[1],
                'publishdate': new[2],
                'createdat': new[3],
                'updatedat': new[4]
            }
            news_list.append(new_info)

        # Return the list of new information as JSON response
        #return jsonify(news_list), 200
        return render_template('news.html',news = news_list)

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'An error occurred'}), 500


@news_bp.route('/delete_new/<int:newsid>', methods=['POST'])
def delete_new(newsid):
    # Call stored procedure to delete a new
    query = "deletenews"
    args = (newsid,)
    db = Database()
    db.execute_query(query,args)

    return jsonify({'message': 'news deleted successfully'}), 200
