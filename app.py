from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import path

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

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        data = request.form.to_dict()
        message = data["message"].strip()
        print(message)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)