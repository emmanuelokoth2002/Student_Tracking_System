from flask import Flask
from users import users_bp
from students import students_bp
from parents import parents_bp
from teachers import teachers_bp
from classes import  classes_bp
from assignments import asignments_bp
from attendance import attendance_bp
from news import news_bp
from fees import fees_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.register_blueprint(users_bp)
app.register_blueprint(students_bp)
app.register_blueprint(parents_bp)
app.register_blueprint(teachers_bp)
app.register_blueprint(classes_bp)
app.register_blueprint(asignments_bp)
app.register_blueprint(attendance_bp)
app.register_blueprint(news_bp)
app.register_blueprint(fees_bp)

if __name__ == '__main__':
    app.run(debug=True)
