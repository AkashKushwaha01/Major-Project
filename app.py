from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# CHANGE 1: RESTORED DATABASE CONNECTION
# This connects to the 'db' container on port 27017
client = MongoClient(host='db', port=27017)
db = client.major_db
collection = db.records

@app.route('/')
def index():
    # CHANGE 2: RESTORED REAL DATA FETCH
    # We are now pulling real data from MongoDB instead of a dummy list
    items = collection.find()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    # This captures the input from your form and saves it to MongoDB
    content = request.form.get('content')
    if content:
        collection.insert_one({'text': content})
    return redirect(url_for('index'))

if __name__ == '__main__':
    # host='0.0.0.0' makes it accessible inside a Docker network
    app.run(host='0.0.0.0', port=5000)