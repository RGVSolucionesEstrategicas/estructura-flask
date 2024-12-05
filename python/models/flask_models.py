from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Length

class RolesForm(FlaskForm):
    id_rol = StringField('ID Rol', validators=[Length(max=50)])
    nombre = StringField('Nombre*', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Registrar')

class UsuariosForm(FlaskForm):
    id_usuario = StringField('ID Usuario', validators=[Length(max=50)])
    id_rol = SelectField('Rol*', validators=[DataRequired(), Length(max=50)])
    id_proveedor = SelectField('Proveedor*', validators=[DataRequired(), Length(max=50)])
    nombre = StringField('Nombre*', validators=[DataRequired(), Length(max=50)])
    correo_electronico = EmailField('Correo electrónico*', validators=[DataRequired(), Length(max=50)])
    contrasena = PasswordField('Contraseña*', validators=[Length(max=255)])
    estatus = SelectField('Estatus',choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')],default='Activo',validators=[DataRequired()])
    submit = SubmitField('Registrar')

class ProveedoresForm(FlaskForm):
    id_proveedor = StringField('ID Proveedor', validators=[Length(max=50)])
    nombre = StringField('Nombre*', validators=[DataRequired(), Length(max=50)])
    rfc = StringField('RFC*', validators=[DataRequired(), Length(max=50)])
    razon_social = StringField('Razón Social*', validators=[DataRequired(), Length(max=50)])
    estatus = SelectField('Estatus',choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')],default='Activo',validators=[DataRequired()])
    submit = SubmitField('Registrar')

class UbicacionesForm(FlaskForm):
    id_ubicacion = StringField('ID Ubicación', validators=[Length(max=50)])
    nombre = StringField('Nombre*', validators=[DataRequired(), Length(max=50)])
    estatus = SelectField('Estatus',choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')],default='Activo',validators=[DataRequired()])
    submit = SubmitField('Registrar')

class ServiciosMedicosForm(FlaskForm):
    id_servicio_medico = StringField('ID Servicio Médico', validators=[Length(max=50)])
    nombre = StringField('Nombre*', validators=[DataRequired(), Length(max=50)])
    estatus = SelectField('Estatus',choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')],default='Activo',validators=[DataRequired()])
    submit = SubmitField('Registrar')

class ClavesOracleForm(FlaskForm):
    clave_oracle = StringField('Clave oracle*', validators=[Length(max=50)])
    clave_cuadro_basico = StringField('Clave cuadro básico', validators=[Length(max=50)])
    descripcion = TextAreaField('Descripción*', validators=[DataRequired(),Length(max=1000)])
    grupo_terapeutico = StringField('Grupo terapeútico', validators=[Length(max=500)])
    forma_farmaceutica = StringField('Forma farmaceútica', validators=[Length(max=500)])
    nombre_generico = StringField('Nombre genérico', validators=[Length(max=500)])
    estatus = SelectField('Estatus',choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')],default='Activo',validators=[DataRequired()])
    submit = SubmitField('Registrar')

class ContratosForm(FlaskForm):
    id_contrato = StringField('ID Contrato', validators=[Length(max=50)])
    id_proveedor = SelectField('Proveedor*', validators=[DataRequired(), Length(max=50)])
    numero_contrato = StringField('Número de contrato*', validators=[DataRequired(), Length(max=50)])
    estatus = SelectField('Estatus',choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')],default='Activo',validators=[DataRequired()])
    submit = SubmitField('Registrar')

class ClavesOracleEnContratoForm(FlaskForm):
    id_clave_oracle_en_contrato = StringField('ID Clave oracle contrato', validators=[Length(max=50)])
    id_contrato = StringField('Contrato*', validators=[DataRequired(), Length(max=255)])
    clave_oracle = StringField('Clave oracle*', validators=[DataRequired(), Length(max=50)])
    cantidad = DecimalField('Cantidad*', validators=[DataRequired()])
    submit = SubmitField('Registrar')

class ClavesOracleEntregadasForm(FlaskForm):
    id_clave_oracle_entregada = StringField('ID clave oracle entregada', validators=[Length(max=50)])
    id_clave_oracle_en_contrato = StringField('ID Clave oracle contrato', validators=[DataRequired(), Length(max=255)])
    id_ubicacion = StringField('Ubicación*', validators=[DataRequired(), Length(max=255)])
    id_servicio_medico = StringField('Servicio médico*', validators=[DataRequired(), Length(max=255)])
    clave_oracle = StringField('Clave oracle*', validators=[DataRequired(), Length(max=50)])
    cantidad_entregada = DecimalField('Cantidad entregada*', validators=[DataRequired()])
    comentarios = StringField('Comentarios', validators=[Length(max=1000)])
    fecha_entrega = DateField('Fecha de entrega*',validators=[DataRequired()])
    submit = SubmitField('Registrar')
