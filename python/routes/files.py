# python/routes/files.py

import os

from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for

from python.models.rds_models import Files
from python.services.s3_boto3 import S3Service

files_bp = Blueprint("files", __name__, url_prefix="/files")

# Determinar el perfil desde variable de entorno
profile = os.getenv("profile", "produccion")

if profile == "prueba-local":
    s3_service = S3Service(use_local_profile=True, profile_name="prueba-local")
else:  # Perfil de producción
    s3_service = S3Service()


@files_bp.route("/", methods=["GET", "POST"])
def files_view():
    """Ruta principal para manejar la subida y listado de archivos."""
    if request.method == "POST":
        file = request.files.get("file")
        if not file:
            flash("Por favor, selecciona un archivo para subir.", "danger")
            return redirect(url_for("files.files_view"))

        try:
            # Subir el archivo a S3
            file_url = s3_service.upload_file(file)
            flash("Archivo subido exitosamente.", "success")
        except Exception as e:
            flash(f"Error al subir el archivo: {e}", "danger")
        return redirect(url_for("files.files_view"))

    # Renderizar la vista principal con la tabla y el formulario
    return render_template("main/files.html")


@files_bp.route("/upload", methods=["POST"])
def upload_file():
    """Ruta para subir un archivo a S3."""
    file = request.files.get("file")
    if not file:
        flash("Por favor, selecciona un archivo para subir.", "danger")
        return redirect(url_for("files.files_view"))

    try:
        # Subir el archivo a S3
        file_url = s3_service.upload_file(file)
        flash("Archivo subido exitosamente.", "success")
    except Exception as e:
        flash(f"Error al subir el archivo: {e}", "danger")
    return redirect(url_for("main.files"))


@files_bp.route("/data", methods=["GET"])
def files_data():
    """Ruta para obtener los archivos en formato JSON."""
    try:
        files = Files.query.order_by(Files.uploaded_at.desc()).all()
        files_list = [
            {
                "filename": file.filename,
                "filepath": file.filepath,
                "uploaded_at": file.uploaded_at.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for file in files
        ]
        return jsonify(files_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@files_bp.route("/generate-presigned-url", methods=["POST"])
def generate_presigned_url():
    """
    Genera y retorna una URL firmada para descargar un archivo de S3.
    """
    try:
        filepath = request.json.get("filepath")
        if not filepath:
            return jsonify({"error": "El campo 'filepath' es obligatorio"}), 400

        presigned_url = s3_service.generate_presigned_url(filepath)
        return jsonify({"presigned_url": presigned_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
