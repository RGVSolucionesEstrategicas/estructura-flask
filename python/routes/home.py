# python/routes/home.py

from flask import Blueprint, flash, redirect, render_template, request, url_for, jsonify
from python.services.s3_service import S3Service
from python.models.rds_models import Files

home_bp = Blueprint("home", __name__)
s3_service = S3Service()


@home_bp.route("/", methods=["GET"])
def inicio():
    """Ruta principal."""
    data = {"activeMenu": "inicio"}
    return render_template("main/inicio.html", **data)


@home_bp.route("/files", methods=["GET", "POST"])
def files():
    """Ruta principal que contiene la tabla y el formulario de subida."""
    if request.method == "POST":
        file = request.files.get("file")
        if not file:
            flash("Por favor, selecciona un archivo para subir.", "danger")
            return redirect(url_for("home.files"))

        try:
            # Sube el archivo a S3
            s3_service.upload_file(file)
            flash("Archivo subido exitosamente.", "success")
        except Exception as e:
            flash(f"Error al subir el archivo: {e}", "danger")
        return redirect(url_for("home.files"))

    # Obtiene los archivos para mostrarlos en la tabla
    try:
        files = Files.query.order_by(Files.uploaded_at.desc()).all()
    except Exception as e:
        files = []
        flash(f"Error al obtener los archivos: {e}", "danger")

    return render_template("main/files.html", files=files)
