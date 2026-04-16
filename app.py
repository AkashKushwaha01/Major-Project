from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

# This connects the Python app to the Database
# We use 'db' because that will be the name of our database container
client = MongoClient(host='db', port=27017)
db = client.major_db
collection = db.records

@app.route('/')
def index():
    items = list(collection.find())
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    user_input = request.form.get('content')
    if user_input:
        collection.insert_one({'text': user_input})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)