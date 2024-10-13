from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_prefixed_env()
login = LoginManager(app)
login.login_view = "login"


from .models import db
from flask_alembic import Alembic

db.init_app(app)
alembic = Alembic()
alembic.init_app(app)

from app import routes
