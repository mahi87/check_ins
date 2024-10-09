from flask import redirect, render_template, request
from app import app, db
from app.models import Contractor


@app.route("/", methods=["GET"])
def home_page():
    contractors_list = Contractor.query.all()
    return render_template("home_page.html", contractors_list=contractors_list)


@app.route("/contractor", methods=["POST", "GET"])
def contractor():
    if request.method == "GET":
        return render_template("contractor_details.html")
    name = request.form["name"]
    occupation = request.form["occupation"]
    salary = request.form["salary"]
    payout_on = request.form["payout_on"]
    contractor = Contractor(
        name=name, occupation=occupation, salary=salary, payout_at=payout_on
    )
    db.session.add(contractor)
    db.session.commit()
    return redirect("/")


@app.route("/contractor/<contractor_id>", methods=["POST"])
def delete_contractor(contractor_id):
    contractor = Contractor.query.get(contractor_id)
    db.session.delete(contractor)
    db.session.commit()
    return redirect("/")
