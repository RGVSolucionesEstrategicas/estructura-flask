from flask import request, render_template
from app import *
from python.models import *


@app.route("/editar_respuestas", methods=["POST"])
def editar_respuestas():
    respuestas = request.form.to_dict()
    for respuesta_id, respuesta_valor in respuestas.items():
        data = CedulasRespuestas.query.get(respuesta_id)
        data.respuesta = respuesta_valor.encode("utf-8").decode("utf-8")
        id_respuesta = respuesta_id
    db.session.commit()
    data = {"activeMenu": "formularios", "activeItem": ""}
    return redirect(url_for("formularios"))


@app.route("/edit_record_html/<string:id>&&<string:table>", methods=["POST"])
@login_required
def edit_record_html(id, table):
    return redirect(url_for("catalogos"))
