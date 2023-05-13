from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "secret key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:test@172.17.0.2/crud_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()

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
    all_data = User.query.all()

    return render_template("index.html", employees = all_data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        # Passing the fields from html
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = User(name, email, phone)

        db.session.add(my_data)
        db.session.commit()


        return redirect(url_for('Index'))
    



if __name__ == "__main__":
    app.run(debug=True)