from flask import(
    render_template, Blueprint, flash, g, redirect, request, session, url_for 
)

import functools

import time

#para encriptar contraseña del usuario
from werkzeug.security import check_password_hash, generate_password_hash

#crear tablas en la bd automaticamentte 
from goodvibesblog.modelos.usuario import Usuario

#importo bd
from goodvibesblog import bd

autenticacion = Blueprint('autenticacion', __name__, url_prefix='/autenticacion')

#Registrar un usuario
@autenticacion.route('/registrar', methods=('GET', 'POST')) #por defecto se usa get pero a la hora de registrar hay que utilizar post
def registrar():
    if request.method == 'POST':
        #capturar lo que nos manda el usuario en los formularios y guardarlos en variables
        nombre = request.form.get('nombre')
        password = request.form.get('password')
        img = request.form.get('img')
        usuario = Usuario(nombre, generate_password_hash(password), img) #objeto usuario a crear por constructor
        error = None
        if not nombre: 
            error = 'Nombre de usuario es obligatorio'
        elif not password:
            error = 'Contraseña obligatoria'
        elif not img:
            error = 'Foto de perfil obligatoria'

        nombre_a_buscar = Usuario.query.filter_by(nombre = nombre).first() #consulta a bd para chequear si el usuario a crear es igual a alguno existente en la bd
        if nombre_a_buscar == None:
            bd.session.add(usuario) #agrega el usuario a la bd
            bd.session.commit()
            return redirect(url_for('autenticacion.login'))
        else:
            error = f'El usuario {nombre} ya esta registrado'       
        flash(error)      
    return render_template('autenticacion/registro.html')

#Iniciar Sesion
@autenticacion.route('/login', methods=( 'GET', 'POST')) 
def login():
    if request.method == 'POST':
        #capturar lo que nos manda el usuario en los formularios y guardarlos en variables
        nombre = request.form.get('nombre')
        password = request.form.get('password')
        
      

        error = None
        
        #verificar si el usuario a logearse existe en la bd
        usuario = Usuario.query.filter_by(nombre = nombre).first() #consulta a bd para chequear si el usuario a crear es igual a alguno existente en la bd
        
        if usuario == None: 
            error = 'El usuario a logearse no existe'
        elif not check_password_hash(usuario.password, password): #la contraseña coincide con el usuario a logearse
            error = 'Contraseña incorrecta'
        
        if error == None:
            session.clear()
            session['user_id'] = usuario.id 
            return redirect(url_for('blog.index')) #redirecciona a la pagina de inicio      
        
        flash(error)    
    
    return render_template('autenticacion/login.html')


@autenticacion.before_app_request
def cargar_usuario_logeado():
    #captura el id del usuario si es que esta logeado
    user_id = session.get('user_id')
    if user_id is None:
        g.usuario = None
    else:
        #obtener un usuario, cargar un usuario el cual esta logueado mediante una consuta a la bd
        g.usuario = Usuario.query.get_or_404(user_id) #obtiene el id o si existe algun error 404 manda el error

@autenticacion.route('/logout')
def cerrar_sesion():
    session.clear()
    return redirect(url_for('blog.index')) 


#esta funcion determina que es necesario logearse para determinadas vistasa
def login_requerido(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.usuario is None: #si el g.usuario es nullo quiere decir que el usuario no esta logeado
            return redirect(url_for('autenticacion.login')) 
        return view(**kwargs)
    return wrapped_view


