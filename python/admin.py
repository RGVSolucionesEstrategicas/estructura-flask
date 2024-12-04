from flask import request, render_template
from app import *
from python.models import *
from python.authentication import *
from python.flask_models import *



@app.route('/catalogos', methods=['POST','GET'])
@login_required
@roles_required(['Admin'])
def catalogos():
    data={ 'activeMenu': 'catalogos', 'activeDefTab':'claves_oracle'}
    # forms
    form_clave_oracle = ClavesOracleForm()
    form_contratos= ContratosForm()
    form_proveedores = ProveedoresForm()
    form_servicios_medicos = ServiciosMedicosForm()
    form_ubicaciones =  UbicacionesForm()
    form_usuarios = UsuariosForm()
    # tablas
    table_claves_oracle=db.session.query(ClavesOracle).all()
    table_proveedores=db.session.query(PortalServiciosProveedores).all()
    table_contratos=db.session.query(PortalServiciosContratos).all()
    table_ubicaciones=db.session.query(PortalServiciosUbicaciones).all()
    table_servicios_medicos=db.session.query(PortalServiciosServiciosMedicos).all()
    table_roles=db.session.query(PortalServiciosRoles).all()   
    table_usuarios=db.session.query(PortalServiciosUsuarios).all()
    # selects
    proveedores_select = [("", "Selecciona una opción")] + [(str(proveedor.id_proveedor), proveedor.nombre) for proveedor in table_proveedores]    
    form_contratos.id_proveedor.choices = proveedores_select
    roles_select = [("", "Selecciona una opción")] + [(str(rol.id_rol), rol.nombre) for rol in table_roles]    
    form_usuarios.id_rol.choices = roles_select
    form_usuarios.id_proveedor.choices = proveedores_select
    return render_template('main/catalogos.html', **data,form_clave_oracle=form_clave_oracle,table_claves_oracle=table_claves_oracle,form_contratos=form_contratos,
                           table_contratos=table_contratos,form_proveedores=form_proveedores,table_proveedores=table_proveedores,form_servicios_medicos=form_servicios_medicos,table_servicios_medicos=table_servicios_medicos,
                           form_ubicaciones=form_ubicaciones,table_ubicaciones=table_ubicaciones,form_usuarios=form_usuarios,table_usuarios=table_usuarios)