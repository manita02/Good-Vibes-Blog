from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for
)

from werkzeug.exceptions import abort

from goodvibesblog.modelos.publicacion import Publicacion

from goodvibesblog.modelos.usuario import Usuario

from goodvibesblog.vistas.autenticacion import login_requerido

from goodvibesblog import bd

from goodvibesblog.vistas.mensaje import obtener_mensaje  

blog = Blueprint('blog', __name__)

#Obtener un usuario por id
def obtener_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return usuario

@blog.route("/")
def index():
    publicaciones = Publicacion.query.all() #obtiene todas las publicaciones que existan en la bd
    bd.session.commit()
    return render_template('blog/index.html', publicaciones = publicaciones, obtener_usuario = obtener_usuario) #este return manda todos estos parametros con la informacion a la pag de index.html

'''
def obtener_mensaje(numero):
    if numero == 1:
        return 'Se ha actualizado la publicacion'
    if numero == 2:
        return 'Se ha eliminado la publicacion'
    if numero == 3:
        return 'Se ha guardado la publicacion'
    else:
        return 'caca bien grande'

@blog.route('/blog/mensaje')
def mensaje(numero):
    #numero = 3
    resultado = obtener_mensaje(numero)
    return render_template('blog/mensaje.html', resultado = resultado)
'''

#crear publicacion
@blog.route('/blog/crear', methods=('GET', 'POST')) 
@login_requerido #entra a la funcion y verifica si el usuario esta logeado para luego poder crear una publicacion
def crear():
    if request.method == 'POST':
        #capturar lo que nos manda el usuario en los formularios y guardarlos en variables
        titulo = request.form.get('titulo')
        cuerpo = request.form.get('cuerpo')
        img = request.form.get('img')
        link = request.form.get('link')
        
        publicacion = Publicacion(g.usuario.id, titulo, cuerpo, img, link) #g.usuario.id obtiene el id del usuario logeado actualmente que ya paso por la funcion verificadora loguin_requerido()
        
        error = None
        if not titulo: 
            error = 'Titulo obligatorio'
        elif not cuerpo:
            error = 'Cuerpo obligatorio'
        elif not img:
            error = 'Imagen obligatoria'
        elif not link:
            error = 'Link obligatorio'

        if error is not  None:
            flash(error)
        else:
            bd.session.add(publicacion)
            bd.session.commit()
            return render_template('mensajes/Mensajee.html', resultado = obtener_mensaje(4, 'Post'))
            #return redirect(url_for('blog.index'))
    
        flash(error)      
    return render_template('blog/crear.html')

#Obtener una publicacion por id
def obtener_publicacion(id, chequear_autor = True):
    publicacion = Publicacion.query.get(id)
    
    #si la publicacion es nula entonces no existe
    if publicacion is None:
        abort(404, f'ID {id} de la publicación no existe')

    if chequear_autor and publicacion.autor != g.usuario.id:
        abort(404)
    
    return publicacion


#Actualizar publicacion
@blog.route('/blog/actualizar/<int:id>', methods=('GET', 'POST')) 
@login_requerido #entra a la funcion y verifica si el usuario esta logeado para luego poder crear una publicacion
def actualizar(id):

    publicacion = obtener_publicacion(id)


    if request.method == 'POST':
        #capturar lo que nos manda el usuario en los formularios y guardarlos en variables
        publicacion.titulo = request.form.get('titulo')
        publicacion.cuerpo = request.form.get('cuerpo')
        publicacion.img = request.form.get('img')
        publicacion.link = request.form.get('link')
            
        error = None
        if not publicacion.titulo: 
            error = 'Titulo obligatorio'
        elif not publicacion.cuerpo:
            error = 'Cuerpo obligatorio'
        elif not publicacion.img:
            error = 'Imagen obligatoria'
        elif not publicacion.link:
            error = 'Link obligatorio'

        if error is not  None:
            flash(error)
        else:
            bd.session.add(publicacion)#agrega un registro y si ese registro no tiene id va a crear un nuevo registro, pero si ese registro si tiene un id lo que va a hacer sera actualizarlo
            bd.session.commit()
            return render_template('mensajes/Mensajee.html', resultado = obtener_mensaje(1, 'Post'))
            #return redirect(url_for('blog.index'))
    
        flash(error)      
    return render_template('blog/actualizar.html', publicacion = publicacion)



#Eliminar una publicacion 
@blog.route('/blog/eliminar/<int:id>')
@login_requerido
def eliminar(id):
    publicacion = obtener_publicacion(id)
    bd.session.delete(publicacion)
    bd.session.commit()

    return render_template('mensajes/Mensajee.html', resultado = obtener_mensaje(2, 'Post'))
    #return redirect(url_for('blog.index'))


