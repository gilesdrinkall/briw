from flask import Flask
from flask import render_template
from flask import request
from source.persistence.database import *


app = Flask(__name__)


@app.route("/briwer", methods=["GET", "POST"])
def add_briwer():

    if request.method == "GET":
        return render_template("briwer_input.html", title="Create New BrIWer")

    if request.method == "POST":
        name = request.form["Name of BrIWer"]
        add_maker_to_db(name)
        return render_template("briwer_submit.html", briwer_name=name)

    else:
        return "Unsupported HTTP Request Type"


@app.route("/round", methods=["GET", "POST"])
def view_add_round():

    if request.method == "GET":
        round_dict = get_maker_name_from_db()
        maker_name = round_dict["maker_name"]
        orders_dict = create_dict_with_subset_data_db("orders", "person_name", "drink_name")
        return render_template("order_input.html", title="Create New Person", round_maker=maker_name, current_order=orders_dict)

    if request.method == "POST":
        name = request.form["name"]
        drink = request.form["drink"]
        create_order(name, drink)
        return render_template("order_submit.html", first_name=name, drink_name=drink)

    else:
        return "Unsupported HTTP Request Type"


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
