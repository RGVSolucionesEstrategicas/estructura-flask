# python/models/rds_models.py

from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from python.models import db


class Users(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    nombre = db.Column(db.String(100), nullable=False)
    correo_electronico = db.Column(db.String(120), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)
    estatus = db.Column(db.String(20), default="Activo", nullable=False)
    fecha_creado = db.Column(db.DateTime, default=datetime.utcnow)

    # Métodos
    def set_password(self, password):
        """Hash the user's password."""
        self.contrasena = generate_password_hash(password)

    def check_password(self, password):
        """Check the user's password."""
        return check_password_hash(self.contrasena, password)

    def get_id(self):
        """Return the user's ID for Flask-Login."""
        return str(self.id)

    def __repr__(self):
        """Represent the user object as a string."""
        return f"<Users(id={self.id}, nombre={self.nombre}, correo={self.correo_electronico})>"
