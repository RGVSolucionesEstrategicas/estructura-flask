# app.py

from python.routes.home import home_bp
from python.routes.authentication import auth_bp
from flask import Flask
from flask_session import Session
from flask_login import LoginManager
from dotenv import load_dotenv
from python.models import db
from python.models.rds_models import Users
import os

# Cargar variables de entorno
load_dotenv()

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configuración de la aplicación
app.secret_key = os.urandom(24)
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = os.urandom(24)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{
        os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializar extensiones
db.init_app(app)
Session(app)


# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"
login_manager.login_message = "Por favor, inicia sesión para acceder a esta página."


@login_manager.user_loader
def load_user(user_id):
    """Cargar un usuario basado en su ID."""
    return Users.query.get(
        user_id
    )


# Filtro para formatear números con comas
@app.template_filter("commafy")
def commafy(value):
    a = round(value, 2)
    return f"{a:,}"


app.jinja_env.filters["commafy"] = commafy

# Registro de Blueprints

app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)

if __name__ == "__main__":
    app.run(debug=True)
