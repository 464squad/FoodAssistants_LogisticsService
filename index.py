from flask import Flask  # import objects from flask model
app = Flask(__name__)  # define app using flask

from flask import jsonify, request #added request

data = [
    { "id":1, "name":"Bread", "quantity":5 },
    { "id":2, "name":"Peanut Butter", "quantity":3 },
    { "id":3, "name":"Jelly", "quantity":2 },
]

sample_submission = {
    "name": "Lameisha Wright",
    "phone": "4702269034",
    "address": "82 Tremont Street SW, Atlanta, GA 30310",
    "distribution": "pickup",
    "residents": 3,
    "items": {
        "grocery": ["chicken", "eggs", "cereal", "bread"],
        "generaHygiene": ["deoderant", "body soap", "tylenol"],
        "feminineHygiene": ["feminine wipes", "regular pads"],
        "cleaningAndHealth": ["all purpose cleaner", "cleaning wipes", "hand sanitizer"]
    }
}

packages = [
    { "id":1, "name":"Grocery" },
    { "id":2, "name":"General Hygiene" },
    { "id":3, "name":"Cleaning/Health Supplies"},
]

package_contents = [
    { "name":"chicken", "household_lt5":1, "household_gte5":1, "quantity":9 },
    { "name":"eggs", "household_lt5":1, "household_gte5":2, "quantity":3 },
    { "name":"cereal", "household_lt5":1, "household_gte5":1, "quantity":9 },
    { "name":"bread", "household_lt5":1, "household_gte5":2, "quantity":7 },
    { "name":"canned food", "household_lt5":4, "household_gte5":8, "quantity":5 },
    { "name":"canned beans", "household_lt5":2, "household_gte5":4, "quantity":9 },
    { "name":"assorted fruit 1", "household_lt5":4, "household_gte5":8, "quantity":2 },
    { "name":"assorted fruit 2", "household_lt5":4, "household_gte5":8, "quantity":0 },
    { "name":"other vegetables", "household_lt5":1, "household_gte5":2, "quantity":5 },
    { "name":"deodorant", "household_lt5":"", "household_gte5":"", "quantity":20 },
    { "name":"body soap", "household_lt5":"", "household_gte5":"", "quantity":17 },
    { "name":"toilet paper", "household_lt5":2, "household_gte5":3, "quantity":8 },
    { "name":"toothbrush", "household_lt5":"", "household_gte5":"", "quantity":4 },
    { "name":"toothpaste", "household_lt5":1, "household_gte5":2, "quantity":11 },
    { "name":"all purpose cleaner", "household_lt5":1, "household_gte5":1, "quantity":2 },
    { "name":"paper towel", "household_lt5":1, "household_gte5":2, "quantity":1 },
    { "name":"dish washing soap", "household_lt5":1, "household_gte5":1, "quantity":10 },
]

fem_package_contents = [
    { "name":"regular tampons", "needs_1":5, "needs_2": 10, "needs_gte3": 15 },
    { "name":"super tampons", "needs_1":5, "needs_2": 10, "needs_gte3": 15 },
    { "name":"regular pads/thin pads", "needs_1":5, "needs_2": 10, "needs_gte3": 15 },
    { "name":"maxi pads", "needs_1":5, "needs_2": 10, "needs_gte3": 15 },
    { "name":"sanitary wipes", "needs_1":1, "needs_2": 1, "needs_gte3": 2 },
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