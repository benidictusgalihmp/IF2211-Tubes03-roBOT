from flask import Flask, render_template, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import path
from component.Tugas import *

db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.DateTime())
    kode = db.Column(db.String(10))
    jenis = db.Column(db.String(10))
    topik = db.Column(db.String(50))
    done = db.Column(db.Integer)

if not path.exists(DB_NAME):
    db.create_all(app=app)
    print("create db")

@app.route("/")
def home():
    return render_template("index.html", response="no message")

@app.route("/message", methods=['GET'])
def getmessage():
    data = request.args
    message = data.get('jsdata').strip()
    response = Tugas.parse(message)
    if response is None:
        response = "Maaf, pesan tidak dikenali"
    return response

if __name__ == "__main__":
    app.run(debug=True)