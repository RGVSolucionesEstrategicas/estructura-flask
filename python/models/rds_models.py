from app import *
from flask_sqlalchemy import SQLAlchemy
import os
from flask import request, redirect, url_for
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import or_,and_,cast, String,func,text

db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# roles
class PortalServiciosRoles(db.Model):
    id_rol = db.Column(db.String(50), primary_key=True, unique=True)
    nombre = db.Column(db.String(50))
    fecha_creado=db.Column(db.DateTime, default=db.func.current_timestamp())

# proveedores
class PortalServiciosProveedores(db.Model):
    id_proveedor = db.Column(db.String(50),primary_key=True,unique=True)
    nombre = db.Column(db.String(50))
    rfc=db.Column(db.String(50),unique=True)
    razon_social=db.Column(db.String(50),unique=True)
    estatus=db.Column(db.String(10),default='Activo')
    fecha_creado=db.Column(db.DateTime, default=db.func.current_timestamp())

# ubicaciones
class PortalServiciosUbicaciones(db.Model):
    id_ubicacion = db.Column(db.String(50),primary_key=True,unique=True)
    nombre = db.Column(db.String(50))
    estatus=db.Column(db.String(10),default='Activo')
    fecha_creado=db.Column(db.DateTime, default=db.func.current_timestamp())

# servicio medico
class PortalServiciosServiciosMedicos(db.Model):
    id_servicio_medico = db.Column(db.String(50),primary_key=True,unique=True)
    nombre = db.Column(db.String(50))
    estatus=db.Column(db.String(10),default='Activo')
    fecha_creado=db.Column(db.DateTime, default=db.func.current_timestamp())

# usuarios
class PortalServiciosUsuarios(db.Model):
    id_usuario = db.Column(db.String(50), primary_key=True, unique=True)
    id_rol=db.Column(db.String(50),db.ForeignKey('portal_servicios_roles.id_rol'))
    id_proveedor=db.Column(db.String(50),db.ForeignKey('portal_servicios_proveedores.id_proveedor'))
    nombre = db.Column(db.String(50), nullable=False)
    correo_electronico = db.Column(db.String(50), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)  # Use String for storing hashed password
    estatus = db.Column(db.String(10),default='Activo')
    fecha_creado=db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self,id_usuario,id_rol,id_proveedor,nombre,correo_electronico,contrasena):
        self.id_usuario = id_usuario
        self.id_rol = id_rol
        self.id_proveedor=id_proveedor
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.contrasena = generate_password_hash(contrasena)  # Hash the password before saving

# claves oracle
class ClavesOracle(db.Model):
    clave_oracle= db.Column(db.String(50), primary_key=True, unique=True)
    clave_cuadro_basico= db.Column(db.String(50),unique=True)
    descripcion=db.Column(db.String(1000))
    grupo_terapeutico= db.Column(db.String(500))   
    forma_farmaceutica= db.Column(db.String(500))   
    nombre_generico= db.Column(db.String(500))
    estatus=db.Column(db.String(50),default='Activo')
    fecha_creado=db.Column(db.DateTime, default=db.func.current_timestamp())

# contratos
class PortalServiciosContratos(db.Model):
    id_contrato= db.Column(db.String(50), primary_key=True, unique=True)
    id_proveedor=db.Column(db.String(50),db.ForeignKey('portal_servicios_proveedores.id_proveedor'))
    numero_contrato=db.Column(db.String(50))
    estatus=db.Column(db.String(50), default='Pendiente')
    fecha_creado=db.Column(db.DateTime, default=db.func.current_timestamp())

# claves oracle en contrato model
class PortalServiciosClavesOracleEnContrato(db.Model):
    id_clave_oracle_en_contrato = db.Column(db.String(50), primary_key=True, unique=True)
    id_contrato= db.Column(db.String(255),db.ForeignKey('portal_servicios_contratos.id_contrato'))
    clave_oracle=db.Column(db.String(50),db.ForeignKey('claves_oracle.clave_oracle'))
    cantidad=db.Column(db.Integer())
    fecha_creado=db.Column(db.DateTime, default=db.func.current_timestamp())

# claves oracle en contrato model
class PortalServiciosClavesOracleEntregadas(db.Model):
    id_clave_oracle_entregada = db.Column(db.String(50), primary_key=True, unique=True)
    id_clave_oracle_en_contrato= db.Column(db.String(255),db.ForeignKey('portal_servicios_claves_oracle_en_contrato.id_clave_oracle_en_contrato'))
    id_ubicacion=db.Column(db.String(255),db.ForeignKey('portal_servicios_ubicaciones.id_ubicacion'))
    id_servicio_medico=db.Column(db.String(255),db.ForeignKey('portal_servicios_servicios_medicos.id_servicio_medico'))
    clave_oracle=db.Column(db.String(50),db.ForeignKey('claves_oracle.clave_oracle'))
    cantidad_entregada=db.Column(db.Integer())
    comentarios=db.Column(db.String(1000))
    fecha_entrega=db.Column(db.DateTime)
    fecha_creado=db.Column(db.DateTime, default=db.func.current_timestamp())
