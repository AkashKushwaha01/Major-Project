from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Connection
mongo_uri = os.environ.get('MONGO_URI', 'mongodb://db:27017/')
client = MongoClient(mongo_uri)
db = client.student_db

@app.route('/')
def index():
    students = list(db.students.find())
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    data = {
        "name": request.form.get('name'),
        "roll_no": request.form.get('roll_no'),
        "email": request.form.get('email'),
        "course": request.form.get('course')
    }
    if data["name"] and data["roll_no"]:
        db.students.insert_one(data)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)