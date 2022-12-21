from flask import Flask  # import objects from flask model
from flask_sqlalchemy import SQLAlchemy

# Boilerplate code
app = Flask(__name__)  # define app using flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:[YOURPOSTGRESPASSWORD]@localhost/flaskapp'
db = SQLAlchemy(app)

# Not sure if you need this. I found it and threw it in looking for solutions to a runtime error 
app.app_context().push()
# Same as above
with app.app_context():
    db.create_all()

# This creates a User table with its columns, and constraints
class User(db.Model) :
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(80),unique = True)
    email = db.Column(db.String(120),unique = True)

    def __init__(self,username,email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

# this is another table that I made to represent a customer. I did not include all info because 
# my inital thought was to put distribution and residents in seperate tables since they both may change based on new orders
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(120), nullable=False)
# This is a test table that was created in the tutorial
user = User(username='newuser', email='newuser@example.com')
db.session.add(user)
db.session.commit()
# This is a route that was in the tutorial. 
    @app.route('/')
    def index():
        return "<h1 style='color:red'>hello flask</h1>"
# Other code to make the stuff work.
if __name__ == "__main__":
    app.run(port=3000, debug=True) 
