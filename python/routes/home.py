# python/routes/home.py

from flask import request, render_template
from app import *
from python.models import *
from sqlalchemy.orm import aliased
from python.authentication import *


@app.route("/", methods=["POST", "GET"])
@login_required
def inicio():
    data = {"activeMenu": "inicio"}
    return render_template("main/inicio.html", **data)


@app.route("/entregas", methods=["POST", "GET"])
@login_required
def entregas():
    data = {"activeMenu": "entregas"}
    return render_template("main/entregas.html", **data)


@app.route("/contratos", methods=["POST", "GET"])
@login_required
def contratos():
    data = {"activeMenu": "contratos"}
    return render_template("main/contratos.html", **data)
