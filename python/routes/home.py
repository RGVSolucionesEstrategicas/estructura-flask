# python/routes/home.py

from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__)


@home_bp.route("/", methods=["GET"])
def inicio():
    """Ruta principal."""
    data = {"activeMenu": "inicio"}
    return render_template("main/inicio.html", **data)


@home_bp.route("/health")
def health():
    return "OK", 200
