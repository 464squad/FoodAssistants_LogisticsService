from flask import Flask  # import objects from flask model
app = Flask(__name__)  # define app using flask

from flask import jsonify

data = [
    { "id":1, "name":"Bread", "quantity":5 },
    { "id":2, "name":"Peanut Butter", "quantity":3 },
    { "id":3, "name":"Jelly", "quantity":2 },
]

@app.route("/")
def index():
    return "Hello World!"

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