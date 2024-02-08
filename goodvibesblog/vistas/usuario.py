from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for
)

from werkzeug.exceptions import abort

from goodvibesblog.modelos.usuario import Usuario

from goodvibesblog.vistas.autenticacion import login_requerido

from goodvibesblog.vistas.autenticacion import cerrar_sesion

from goodvibesblog.vistas.mensaje import obtener_mensaje  

from goodvibesblog.vistas.blog import verificar_publicaciones_usuario

from goodvibesblog import bd

usuario = Blueprint('usuario', __name__)

#Obtener un usuario por id
def obtener_usuario(id):
    usuario = Usuario.query.get(id)
    #si el usuario es nulo entonces no existe
    if usuario is None:
        abort(404, f'User ID {id} does not exist')
    return usuario

#Actualizar usuario
@usuario.route('/usuario/actualizar/<int:id>', methods=('GET', 'POST')) 
@login_requerido #entra a la funcion y verifica si el usuario esta logeado para luego poder crear una publicacion
def actualizar(id):
    usuario = obtener_usuario(id)

    if request.method == 'POST':
        #capturar lo que nos manda el usuario en los formularios y guardarlos en variables
        usuario.nombre = request.form.get('nombre')
        usuario.img = request.form.get('img')
        
            
        error = None
        if not usuario.nombre: 
            error = 'Name is required'
        elif not usuario.img:
            error = 'Perfil photo is required'

        if error is not  None:
            flash(error)
        else:
            bd.session.add(usuario)#agrega un registro y si ese registro no tiene id va a crear un nuevo registro, pero si ese registro si tiene un id lo que va a hacer sera actualizarlo
            bd.session.commit()
            return render_template('mensajes/Mensajee.html', resultado = obtener_mensaje(3, 'User'))
            #return redirect(url_for('blog.index'))
    
        flash(error)      
    return render_template('usuario/actualizar.html', usuario = usuario)



#Eliminar un usuario 
@usuario.route('/usuario/eliminar/<int:id>')
@login_requerido
def eliminar(id):
    usuario = obtener_usuario(id)
    error = None

    if verificar_publicaciones_usuario(usuario.id) > 0: 
       error = 'This user has posts posted on the blog. First delete all the posts made by this user, and then you can delete this user'
       flash(error) 
    else: 
        bd.session.delete(usuario)
        bd.session.commit()
        cerrar_sesion()
        return render_template('mensajes/Mensajee.html', resultado = obtener_mensaje(2, 'User'))
        return redirect(url_for('blog.index'))
    return redirect(url_for('usuario.actualizar', id = usuario.id)) 