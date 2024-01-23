from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
# 8c7Pno01AtZ0ewuf
app.config["MONGO_URI"] = "mongodb+srv://illustrator5223:8c7Pno01AtZ0ewuf@cluster0.ug5yjmy.mongodb.net/ngo"
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run()

@app.route('/handle_data', methods=['POST'])
def handle_data():
    name = request.form['name'];
    email = request.form['email'];


    db.users.insert_one({
        'name': name,
        'email': email,
    })
    return render_template('trial.html')
