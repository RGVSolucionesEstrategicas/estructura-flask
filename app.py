# app.py

from markupsafe import Markup
from flask import Flask, session
import flask

flask.Markup = Markup
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

from flask_security import (
    Security,
    SQLAlchemyUserDatastore,
    auth_required,
    current_user,
)
from flask_security.models import fsqla_v3 as fsqla
from flask_session import Session
from flask import Flask, session
from dotenv import load_dotenv
import os

from python.routes import *
from python.models import *
from python.services import *


@app.template_filter("commafy")
def commafy(value):
    a = round(value, 2)
    return f"{a:,}"
@app.route("/")
def home():
    return "¡Bienvenido a mi aplicación Flask!"

app.jinja_env.filters["commafy"] = commafy

app.secret_key = os.urandom(24)

app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = os.urandom(24)

Session(app)

if __name__ == "__main__":
    app.run(debug=True)
