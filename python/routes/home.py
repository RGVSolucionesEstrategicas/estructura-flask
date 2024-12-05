# python/routes/home.py

from flask import Blueprint, render_template
from flask_login import login_required

home_bp = Blueprint("home", __name__)


@home_bp.route("/", methods=["GET", "POST"])
@login_required
def inicio():
    data = {"activeMenu": "inicio"}
    return render_template("main/inicio.html", **data)


@home_bp.route("/entregas", methods=["GET", "POST"])
@login_required
def entregas():
    data = {"activeMenu": "entregas"}
    return render_template("main/entregas.html", **data)


@home_bp.route("/contratos", methods=["GET", "POST"])
@login_required
def contratos():
    data = {"activeMenu": "contratos"}
    return render_template("main/contratos.html", **data)
