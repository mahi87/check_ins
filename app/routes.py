from flask import redirect, render_template, request
from app import app, db
from app.models import Contractor


@app.route("/", methods=["GET", "POST"])
def home_page():
    contractors_list = Contractor.query.all()
    return render_template("home_page.html", contractors_list=contractors_list)


@app.route("/contractors", methods=["POST", "GET"])
def contractor_details():
    return render_template("contractor_details.html")


@app.route("/contractor", methods=["POST"])
def contractor():
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


@app.route("/contractor/<contractor_id>", methods=["POST", "GET"])
def remove_contractor(contractor_id):
    contractor = Contractor.query.filter_by(id=contractor_id).all()
    db.session.delete(contractor)
    db.session.commit()
    return redirect("/")
