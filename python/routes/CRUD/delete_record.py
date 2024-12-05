from app import *
from python.models import *
from flask import render_template


@app.route("/delete/<string:id>&&<string:table>", methods=["POST"])
@login_required
def delete(id, table):
    return redirect(url_for("catalogos"))
