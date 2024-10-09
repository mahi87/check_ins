from flask import Flask

app = Flask(__name__)
app.config.from_prefixed_env()

from .models import db
from flask_alembic import Alembic

db.init_app(app)
alembic = Alembic()
alembic.init_app(app)

from app import routes
