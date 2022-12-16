from flask import Flask  # import objects from flask model
app = Flask(__name__)  # define app using flask

from flask import jsonify, request #added request

data = [
    { "id":1, "name":"Bread", "quantity":5 },
    { "id":2, "name":"Peanut Butter", "quantity":3 },
    { "id":3, "name":"Jelly", "quantity":2 },
]

sample_submission1 = {
    "name": "Lameisha Wright",
    "phone": "4702269034",
    "address": "82 Tremont Street SW, Atlanta, GA 30310",
    "distribution": "pickup",
    "residents": 3,
    "numFeminineNeeds":3,
    "items": {
        "grocery": ["chicken", "eggs", "cereal", "bread"],
        "generalHygiene": ["deodorant", "body soap", "toothbrush"],
        "feminineHygiene": ["sanitary wipes", "regular pads"],
        "cleaningAndHealth": ["all purpose cleaner", "paper towel", "dish washing soap"]
    }
}

sample_submission2 = {
    "name": "Lameisha Wright",
    "phone": "4702269034",
    "address": "82 Tremont Street SW, Atlanta, GA 30310",
    "distribution": "pickup",
    "residents": 3,
    "numFeminineNeeds":3,
    "items": {
        "grocery": ["chicken", "eggs", "cereal", "bread", "canned food", "canned beans", "assorted fruit 1", "assorted fruit 2", "other vegetables"],
        "generalHygiene": ["deodorant", "body soap", "toilet paper", "toothbrush", "toothpaste"],
        "feminineHygiene": ["regular tampons", "super tampons", "regular pads", "maxi pads", "sanitary wipes"],
        "cleaningAndHealth": ["all purpose cleaner", "paper towel", "dish washing soap"]
    }
}

package_contents = {
    "chicken":{ "household_lt5":1, "household_gte5":1, "quantity":9 },
    "eggs":{ "household_lt5":1, "household_gte5":2, "quantity":3 },
    "cereal":{ "household_lt5":1, "household_gte5":1, "quantity":9 },
    "bread":{ "household_lt5":1, "household_gte5":2, "quantity":7 },
    "canned food":{ "household_lt5":4, "household_gte5":8, "quantity":5 },
    "canned beans":{ "household_lt5":2, "household_gte5":4, "quantity":9 },
    "assorted fruit 1":{ "household_lt5":4, "household_gte5":8, "quantity":2 },
    "assorted fruit 2":{ "household_lt5":4, "household_gte5":8, "quantity":0 },
    "other vegetables":{ "household_lt5":1, "household_gte5":2, "quantity":5 },
    "deodorant":{ "household_lt5":"", "household_gte5":"", "quantity":20 },
    "body soap":{ "household_lt5":"", "household_gte5":"", "quantity":17 },
    "toilet paper":{ "household_lt5":2, "household_gte5":3, "quantity":8 },
    "toothbrush":{ "household_lt5":"", "household_gte5":"", "quantity":4 },
    "toothpaste":{ "household_lt5":1, "household_gte5":2, "quantity":11 },
    "all purpose cleaner":{ "household_lt5":1, "household_gte5":1, "quantity":2 },
    "paper towel":{ "household_lt5":1, "household_gte5":2, "quantity":1 },
    "dish washing soap":{ "household_lt5":1, "household_gte5":1, "quantity":10 },
}

fem_package_contents = {
    "regular tampons": { "needs_1":5, "needs_2": 10, "needs_gte3": 15, "quantity":14 },
    "super tampons": { "needs_1":5, "needs_2": 10, "needs_gte3": 15, "quantity":11 },
    "regular pads": { "needs_1":5, "needs_2": 10, "needs_gte3": 15, "quantity":24 },
    "maxi pads": { "needs_1":5, "needs_2": 10, "needs_gte3": 15, "quantity":4 },
    "sanitary wipes": { "needs_1":1, "needs_2": 1, "needs_gte3": 2, "quantity": 3 },
}

def calc_available(quantity, amount_needed):
    if quantity >= amount_needed:
        return amount_needed
    else:
        return quantity

def calc_distribution_num(package_type, item_name, num_residents, num_fem_needs):
    if package_type == "feminineHygiene":
        if item_name in fem_package_contents.keys():
            item = fem_package_contents[item_name]
            if num_fem_needs == 1:
                return calc_available(item["quantity"], item["needs_1"])
            elif num_fem_needs == 2:
                return calc_available(item["quantity"], item["needs_2"])
            else:
                return calc_available(item["quantity"], item["needs_gte3"])
                
        else: return 0
    else:
        if item_name in package_contents.keys():
            item = package_contents[item_name]
            if num_residents < 5:
                return calc_available(item["quantity"], item["household_lt5"] if item["household_lt5"] != "" else num_residents )
            else:
                return calc_available(item["quantity"], item["household_gte5"] if item["household_gte5"] != "" else num_residents )

        else: return 0

@app.route("/handle-submission", methods=["POST"])
def submission_post():
    submission = request.json
    num_residents = submission["residents"]
    num_fem_needs = submission["numFeminineNeeds"]
    distribution = {}

    for package_type in submission["items"].keys():
        for item_name in submission["items"][package_type]:
            distribution[item_name] = calc_distribution_num(package_type, item_name, num_residents, num_fem_needs)
    
    print(distribution)
    return jsonify(distribution)

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