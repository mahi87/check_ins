from flask import Flask, render_template

app = Flask(__name__)
app.config.from_prefixed_env()

from models import db
from flask_alembic import Alembic

db.init_app(app)
alembic = Alembic()
alembic.init_app(app)


@app.route("/", methods=["Get"])
def home_page():

    return render_template("home_page.html")
