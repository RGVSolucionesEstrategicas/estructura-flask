# python/routes/users.py

from flask import Blueprint, flash, redirect, render_template, request, url_for

from python.models.rds_models import Users, db

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("/", methods=["GET"])
def users_view():
    """Ruta principal para listar usuarios."""
    users = Users.query.order_by(Users.fecha_creado.desc()).all()
    return render_template("crud/crud.html", users=users)


@users_bp.route("/create", methods=["POST"])
def create_user():
    """Crear un nuevo usuario."""
    try:
        nombre = request.form.get("nombre")
        correo_electronico = request.form.get("correo_electronico")
        contrasena = request.form.get("contrasena")

        if not (nombre and correo_electronico and contrasena):
            flash("Todos los campos son obligatorios.", "danger")
            return redirect(url_for("users.users_view"))

        new_user = Users(nombre=nombre, correo_electronico=correo_electronico)
        new_user.set_password(contrasena)
        db.session.add(new_user)
        db.session.commit()

        flash("Usuario creado exitosamente.", "success")
        return redirect(url_for("users.users_view"))
    except Exception as e:
        db.session.rollback()
        flash(f"Error al crear el usuario: {e}", "danger")
        return redirect(url_for("users.users_view"))


@users_bp.route("/update/<int:user_id>", methods=["GET", "POST"])
def update_user(user_id):
    """Actualizar un usuario existente."""
    try:
        user = Users.query.get_or_404(user_id)

        if request.method == "GET":
            return render_template("crud/editar.html", user=user)

        # Procesar el formulario para actualizar los datos
        user.nombre = request.form.get("nombre", user.nombre)
        user.correo_electronico = request.form.get(
            "correo_electronico", user.correo_electronico
        )
        contrasena = request.form.get("contrasena")
        if contrasena:
            user.set_password(contrasena)

        db.session.commit()
        flash("Usuario actualizado exitosamente.", "success")
        return redirect(url_for("users.users_view"))
    except Exception as e:
        db.session.rollback()
        flash(f"Error al actualizar el usuario: {e}", "danger")
        return redirect(url_for("users.users_view"))


@users_bp.route("/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    """Eliminar un usuario."""
    try:
        user = Users.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        flash("Usuario eliminado exitosamente.", "success")
        return redirect(url_for("users.users_view"))
    except Exception as e:
        db.session.rollback()
        flash(f"Error al eliminar el usuario: {e}", "danger")
        return redirect(url_for("users.users_view"))
