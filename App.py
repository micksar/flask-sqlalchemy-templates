from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "secret key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:test@mysql_container/crud_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id =    db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    #Class constructor
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

@app.route('/')
def Index():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)