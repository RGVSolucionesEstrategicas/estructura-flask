# python/models/rds_models.py

from python.models import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id_usuario = db.Column(db.String(50), primary_key=True, unique=True)
    nombre = db.Column(db.String(50), nullable=False)
    correo_electronico = db.Column(db.String(50), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)
    estatus = db.Column(db.String(10), default="Activo")
    fecha_creado = db.Column(db.DateTime, default=db.func.current_timestamp())

    def set_password(self, password):
        self.contrasena = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.contrasena, password)

    def get_id(self):
        return self.id_usuario
