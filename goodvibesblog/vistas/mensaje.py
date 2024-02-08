from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for
)

from werkzeug.exceptions import abort

mensaje_bp = Blueprint('mensaje', __name__)

def obtener_mensaje(numero, string):
    if numero == 1:
        return string + ' updated successfully!!'
    if numero == 2:
        return string + ' deleted successfully!!'
    if numero == 3:
        return string + ' saved successfully!!'
    if numero == 4:
        return string + ' created successfully!!'   
    if numero == 5:
        return string + ' logged in successfully!!'  
    else:
        return 'error '+ string

@mensaje_bp.route('/mensajes/<int:id>')
def mensaje(numero, string):
    #numero = 3
    resultado = obtener_mensaje(numero, string)
    return render_template('mensajes/Mensajee.html', resultado = resultado)