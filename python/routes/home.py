# python/routes/home.py

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required

from python.services.s3_service import S3Service

home_bp = Blueprint("home", __name__)

s3_service = S3Service()


@home_bp.route("/", methods=["GET", "POST"])
# @login_required
def inicio():
    data = {"activeMenu": "inicio"}
    return render_template("main/inicio.html", **data)


@home_bp.route("/upload", methods=["GET", "POST"])
def upload_file():
    """Ruta para manejar la subida de archivos."""
    data = {"activeMenu": "upload"}
    if request.method == "POST":
        file = request.files.get("file")
        if not file:
            flash("Por favor, selecciona un archivo para subir.", "danger")
            return redirect(url_for("home.upload_file"))

        # Sube el archivo a S3
        try:
            file_url = s3_service.upload_file(file, file.filename)
            flash(f"Archivo subido exitosamente", "success")
            return redirect(url_for("home.upload_file"))
        except Exception as e:
            flash(f"Error al subir el archivo: {e}", "danger")
            return redirect(url_for("home.upload_file"))

    return render_template("main/upload.html", **data)
