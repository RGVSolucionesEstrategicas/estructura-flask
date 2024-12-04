from flask import request, render_template,session
from app import *
from python.models import *
from sqlalchemy import or_,cast, String,func
from functools import wraps  # Import wraps here
from python.send_email import *
import secrets
import string

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'id_usuario' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def roles_required(roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'id_usuario' not in session:
                return redirect(url_for('login'))
            elif session.get('rol') not in roles:
                return redirect('/')
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/authentication/login')
def login():
    return render_template('authentication/login.html')

@app.route('/login_submit', methods=['POST'])
def login_submit():
    email = request.form['email']
    contrasena = request.form['password']
    user = PortalServiciosUsuarios.query.filter(PortalServiciosUsuarios.correo_electronico==email).first()
    if user!=None:
        if check_password_hash(user.contrasena, contrasena):
            session['id_usuario'] = user.id_usuario
            session['nombre'] = user.nombre
            session['correo'] = user.correo_electronico
            rol=PortalServiciosRoles.query.filter(PortalServiciosRoles.id_rol==user.id_rol).first()
            session['rol'] = rol.nombre
            print(rol.nombre)
            return redirect('/')  # Redirect back to the form
        else:
            print("Password is incorrect!")
            return redirect(url_for('login'))  # Redirect back to the form
    else:
        print("Email doesn't exist!")
        return redirect(url_for('login'))  # Redirect back to the form
    
@app.route('/authentication/forgotpassword')
def forgotpassword():
    return render_template('authentication/forgotpassword.html')

@app.route('/forgotpassword_submit', methods=['POST'])
def forgotpassword_submit():
    email = request.form['email']
    user = PortalServiciosUsuarios.query.filter(PortalServiciosUsuarios.correo_electronico==email).first()
    if user!=None:
        # envia correo
        alphabet = string.ascii_letters + string.digits
        contrasena = ''.join(secrets.choice(alphabet) for i in range(20))
        forgot_password_email(email,contrasena)
        user.contrasena=generate_password_hash(contrasena)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        print("Email doesn't exist!")
        return redirect(url_for('/authentication/forgotpassword'))

@app.route('/logout')
def logout():
    session.pop('id_usuario', None)
    session.pop('nombre', None)
    session.pop('jurisdiccion', None)
    session.pop('correo', None)
    session.pop('rol', None)
    return redirect(url_for('login'))
