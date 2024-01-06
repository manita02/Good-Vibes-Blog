from datetime import datetime
from goodvibesblog import bd

class Publicacion(bd.Model):
    __tablename__ = 'publicaciones' #nombre de la tabla de la bd
    id = bd.Column(bd.Integer, primary_key = True) #columnas y campos de la tabla en la base de datos
    autor = bd.Column(bd.Integer, bd.ForeignKey('usuarios.id'), nullable = False) #un usuario puede tener muchas publicaciones --> relacion de 1 a muchos
    titulo = bd.Column(bd.String(100))
    cuerpo = bd.Column(bd.Text)
    img = bd.Column(bd.String(500))
    link = bd.Column(bd.String(500))
    fecha = bd.Column(bd.DateTime, nullable = False, default = datetime.utcnow) #valor por defecto para obtener la fecha actual en el momento en que se crea la publicacion

    #constructor
    def __init__(self, autor, titulo, cuerpo, img, link) -> None:
        self.autor = autor
        self.titulo = titulo
        self.cuerpo = cuerpo
        self.img = img
        self.link = link

    #para mostrar la publicacion
    def __repr__(self) -> str: #devuelve un string --> str
        return f'Publicacion: {self.titulo}'