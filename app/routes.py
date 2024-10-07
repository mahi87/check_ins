from flask import render_template
from app import app


@app.route("/", methods=["Get"])
def home_page():

    return render_template("home_page.html")
