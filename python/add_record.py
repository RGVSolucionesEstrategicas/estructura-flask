from flask import request, render_template
from app import *
from python.models import *
from python.authentication import *
from python.flask_models import *
import secrets
import string

def id_generator(id,prefix):
    try:
        x=1+int(id[2:])
        id=prefix+str(x)
    except:
        id=prefix+'1'
    return id

@app.route('/catalogos/proveedores', methods=['POST','GET'])
@login_required
@roles_required(['Admin'])
def proveedores():
    data={ 'activeMenu': 'catalogos', 'activeDefTab':'claves_oracle'}
    form_proveedores = ProveedoresForm()
    if form_proveedores.validate_on_submit():
        id = db.session.query(PortalServiciosProveedores).order_by(PortalServiciosProveedores.id_proveedor.desc()).first()
        if id is None:
            id = 'PR1'
        else:
            id=id_generator(id.id_proveedor ,'PR')
        proveedor = PortalServiciosProveedores(
            id_proveedor=id,
            nombre=form_proveedores.nombre.data,
            rfc=form_proveedores.rfc.data,
            razon_social=form_proveedores.razon_social.data
        )
        db.session.add(proveedor)
        db.session.commit()
    return redirect(url_for('catalogos'))

@app.route('/catalogos/claves_oracle', methods=['POST','GET'])
@login_required
@roles_required(['Admin'])
def claves_oracle():
    form_clave_oracle = ClavesOracleForm()
    if form_clave_oracle.validate_on_submit():
        clave_oracle = ClavesOracle(
            clave_oracle=form_clave_oracle.clave_oracle.data,
            clave_cuadro_basico=form_clave_oracle.clave_cuadro_basico.data,
            descripcion=form_clave_oracle.descripcion.data,
            grupo_terapeutico=form_clave_oracle.grupo_terapeutico.data,
            forma_farmaceutica=form_clave_oracle.forma_farmaceutica.data,
            nombre_generico=form_clave_oracle.nombre_generico.data
        )
        db.session.add(clave_oracle)
        db.session.commit()
    return redirect(url_for('catalogos'))

@app.route('/catalogos/contratos', methods=['POST','GET'])
@login_required
@roles_required(['Admin'])
def add_contratos():
    form_contratos= ContratosForm()
    table_proveedores=db.session.query(PortalServiciosProveedores).all()
    proveedores_select = [("", "Selecciona una opción")] + [(str(proveedor.id_proveedor), proveedor.nombre) for proveedor in table_proveedores]    
    form_contratos.id_proveedor.choices = proveedores_select
    if form_contratos.validate_on_submit():
        id = db.session.query(PortalServiciosContratos).order_by(PortalServiciosContratos.id_contrato.desc()).first()
        if id is None:
            id = 'CO1'
        else:
            id=id_generator(id.id_contrato ,'CO')
        contrato = PortalServiciosContratos(
            id_contrato=id,
            id_proveedor=form_contratos.id_proveedor.data,
            numero_contrato=form_contratos.numero_contrato.data
        )
        db.session.add(contrato)
        db.session.commit()
    return redirect(url_for('catalogos'))

@app.route('/catalogos/servicios_medicos', methods=['POST','GET'])
@login_required
@roles_required(['Admin'])
def servicios_medicos():
    form_servicios_medicos = ServiciosMedicosForm()
    id = db.session.query(PortalServiciosServiciosMedicos).order_by(PortalServiciosServiciosMedicos.id_servicio_medico.desc()).first()
    if form_servicios_medicos.validate_on_submit():
        id = db.session.query(PortalServiciosServiciosMedicos).order_by(PortalServiciosServiciosMedicos.id_servicio_medico.desc()).first()
        if id is None:
            id = 'SM1'
        else:
            id=id_generator(id.id_servicio_medico ,'SM')
        servicio_medico = PortalServiciosServiciosMedicos(
            id_servicio_medico=id,
            nombre=form_servicios_medicos.nombre.data
        )
        db.session.add(servicio_medico)
        db.session.commit()
    return redirect(url_for('catalogos'))

@app.route('/catalogos/ubicaciones', methods=['POST','GET'])
@login_required
@roles_required(['Admin'])
def ubicaciones():
    form_ubicaciones =  UbicacionesForm()
    if form_ubicaciones.validate_on_submit():
        id = db.session.query(PortalServiciosUbicaciones).order_by(PortalServiciosUbicaciones.id_ubicacion.desc()).first()
        if id is None:
            id = 'UB1'
        else:
            id=id_generator(id.id_ubicacion ,'UB')
        ubicacion = PortalServiciosUbicaciones(
            id_ubicacion=id,
            nombre=form_ubicaciones.nombre.data
        )
        db.session.add(ubicacion)
        db.session.commit()
    return redirect(url_for('catalogos'))

@app.route('/catalogos/usuarios', methods=['POST','GET'])
@login_required
@roles_required(['Admin'])
def usuarios():
    form_usuarios = UsuariosForm()
    table_proveedores=db.session.query(PortalServiciosProveedores).all()
    proveedores_select = [("", "Selecciona una opción")] + [(str(proveedor.id_proveedor), proveedor.nombre) for proveedor in table_proveedores]    
    table_roles=db.session.query(PortalServiciosRoles).all()   
    roles_select = [("", "Selecciona una opción")] + [(str(rol.id_rol), rol.nombre) for rol in table_roles]    
    form_usuarios.id_rol.choices = roles_select
    form_usuarios.id_proveedor.choices = proveedores_select
    if form_usuarios.validate_on_submit():
        id = db.session.query(PortalServiciosUsuarios).order_by(PortalServiciosUsuarios.id_usuario.desc()).first()
        alphabet = string.ascii_letters + string.digits
        if id is None:
            id = 'US1'
        else:
            id=id_generator(id.id_usuario ,'US')
        usuario = PortalServiciosUsuarios(
            id_usuario=id,
            id_rol=form_usuarios.id_rol.data,
            id_proveedor=form_usuarios.id_proveedor.data,
            nombre=form_usuarios.nombre.data,
            correo_electronico=form_usuarios.correo_electronico.data,
            contrasena=''.join(secrets.choice(alphabet) for i in range(20))
        )
        db.session.add(usuario)
        db.session.commit()
    return redirect(url_for('catalogos'))
