# python/routes/authentication.py

from flask import Blueprint, request, render_template, session, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from python.models.rds_models import Users
from python.models import db
import secrets
import string

auth_bp = Blueprint(
    "auth", __name__, url_prefix="/authentication"
)


@auth_bp.route("/login")
def login():
    return render_template("authentication/login.html")


@auth_bp.route("/login_submit", methods=["POST"])
def login_submit():
    email = request.form["email"]
    contrasena = request.form["password"]
    user = Users.query.filter(Users.correo_electronico == email).first()
    if user and check_password_hash(user.contrasena, contrasena):
        session["id_usuario"] = user.id_usuario
        session["nombre"] = user.nombre
        session["correo"] = user.correo_electronico
        return redirect("/")
    return redirect(url_for("auth.login"))


@auth_bp.route("/forgotpassword")
def forgot_password():
    return render_template("authentication/forgotpassword.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
