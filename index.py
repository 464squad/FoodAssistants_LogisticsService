from flask import Flask  # import objects from flask model
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # define app using flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:[PASSWORDFORPOSTGRES]@localhost/flaskapp'
db = SQLAlchemy(app)



class User(db.Model) :
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(80),unique = True)
    email = db.Column(db.String(120),unique = True)

    def __init__(self,username,email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    

from flask import jsonify, request #added request

data = [
    { "id":1, "name":"Bread", "quantity":5 },
    { "id":2, "name":"Peanut Butter", "quantity":3 },
    { "id":3, "name":"Jelly", "quantity":2 },
]

@app.route('/readLogistics', methods=['GET'])
def returnAll():
    return jsonify({'data' : data})

@app.route("/")
def index():
    return "Hello World!"

#POST
@app.route("/lang", methods = ["POST"])
def logistics_post():
    data = {'name': request.json['name']}
    data.append(data)
    return jsonify({'data': data})

@app.route("/api/<id>", methods=["DELETE"])
def logistics_delete(id):
    # Delete record with given id
    index = -1

    for i in range(len(data)):
        if data[i]["id"] == int(id):
            index = i
            break

    if index == -1: 
        return jsonify(
            message=f"Could not find record with id {id}",
            category="error",
            status=404
        )
    else:
        data.pop(index)

        return jsonify(
            message=f"Successfully deleted record with id {id}",
            category="success",
            data=data,
            status=200
        )

if __name__ == "__main__":
    app.run(port=3000, debug=True)  # run app on port 3000