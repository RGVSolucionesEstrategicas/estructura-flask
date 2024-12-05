# python/routes/authentication.py


from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_login import login_user

from python.models import db
from python.models.rds_models import Users

auth_bp = Blueprint("auth", __name__, url_prefix="/authentication")


@auth_bp.route("/login")
def login():
    return render_template("authentication/login.html")


@auth_bp.route("/signin")
def signin():
    return render_template("authentication/signin.html")


@auth_bp.route("/add_user", methods=["POST"])
def add_user():
    """Crea un nuevo usuario."""
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    # Verificar si el usuario ya existe
    existing_user = Users.query.filter_by(correo_electronico=email).first()
    if existing_user:
        flash("El correo ya está registrado. Por favor, usa otro.", "danger")
        return redirect(url_for("auth.signin"))

		# Verificar si los campos están vacíos
    if not email or not password or not name:
        flash("Todos los campos son obligatorios.", "danger")
        return redirect(url_for("auth.signin"))

    # Crear un nuevo usuario
    new_user = Users(nombre=name, correo_electronico=email)
    new_user.set_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
        flash("Usuario creado exitosamente. Ahora puedes iniciar sesión.", "success")
        return redirect(url_for("auth.login"))
    except Exception as e:
        db.session.rollback()
        flash("Ocurrió un error al crear el usuario. Inténtalo nuevamente.", "danger")
        print(f"Error al crear el usuario: {e}")
        return redirect(url_for("auth.signin"))


@auth_bp.route("/login_submit", methods=["POST"])
def login_submit():
    """Autentica al usuario."""
    email = request.form.get("email")
    contrasena = request.form.get("password")

    # Verificar si los campos están vacíos
    if not email or not contrasena:
        flash("Todos los campos son obligatorios.", "danger")
        return redirect(url_for("auth.login"))

    # Buscar al usuario en la base de datos
    user = Users.query.filter_by(correo_electronico=email).first()
    if not user:
        flash("El correo electrónico no está registrado.", "danger")
        return redirect(url_for("auth.login"))

    # Verificar la contraseña
    if not user.check_password(contrasena):
        flash("Contraseña incorrecta. Inténtalo nuevamente.", "danger")
        return redirect(url_for("auth.login"))

    # Establecer al usuario como autenticado
    login_user(user)

    flash(f"¡Bienvenido, {user.nombre}!", "success")
    return redirect(url_for("home.inicio"))


@auth_bp.route("/forgotpassword")
def forgot_password():
    return render_template("authentication/forgotpassword.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
