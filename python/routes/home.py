# python/routes/home.py

from flask import Blueprint, flash, redirect, render_template, request, url_for, jsonify


from python.services.s3_service import S3Service

from python.models.rds_models import Files


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
            file_url = s3_service.upload_file(file)
            flash(f"Archivo subido exitosamente: {file_url}", "success")
            return redirect(url_for("home.upload_file"))
        except Exception as e:
            flash(f"Error al subir el archivo: {e}", "danger")
            return redirect(url_for("home.upload_file"))

    return render_template("main/upload.html", **data)


@home_bp.route("/files", methods=["GET"])
def files():
    """Ruta para obtener todos los archivos desde la base de datos."""
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


@home_bp.route("/files_view", methods=["GET"])
def files_view():
    """Vista para mostrar los archivos en la tabla."""
    return render_template("partials/tabla_archivos.html")
