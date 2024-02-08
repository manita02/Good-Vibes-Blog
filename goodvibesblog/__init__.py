from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Cargar configuraciones
app.config.from_object('configuracion.Desarrollo')
bd = SQLAlchemy(app)

#Importar vistas
from goodvibesblog.vistas.autenticacion import autenticacion #importa el blueprint
app.register_blueprint(autenticacion) #registrar el blueprint en mi aplicacion

from goodvibesblog.vistas.blog import blog
app.register_blueprint(blog)

from goodvibesblog.vistas.usuario import usuario
app.register_blueprint(usuario)


from goodvibesblog.vistas.mensaje import mensaje_bp
app.register_blueprint(mensaje_bp)






#bd.create_all()
