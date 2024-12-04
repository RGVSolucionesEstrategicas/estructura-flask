

from markupsafe import Markup
from flask import Flask,session
import flask
flask.Markup = Markup
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

from flask_security import Security, SQLAlchemyUserDatastore, auth_required,current_user
from flask_security.models import fsqla_v3 as fsqla
from flask_session import Session
from flask import Flask,session
from dotenv import load_dotenv
import os
from python.admin import *
from python.home import *
from python.models import *
from python.delete_record import *
from python.add_record import *
from python.edit_record import *
from python.flask_models import *


@app.template_filter('commafy')
def commafy(value):
    a=round(value,2)
    return f"{a:,}"

app.jinja_env.filters['commafy'] = commafy

app.secret_key = os.urandom(24)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)  # You should use a secure key in production

Session(app)

if __name__ == '__main__':
    app.run(debug=True)
