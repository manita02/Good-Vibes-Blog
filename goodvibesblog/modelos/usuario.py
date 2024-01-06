from goodvibesblog import bd

class Usuario(bd.Model):
    __tablename__ = 'usuarios' #nombre de la tabla de la bd
    id = bd.Column(bd.Integer, primary_key = True) #columnas y campos de la tabla en la base de datos
    nombre = bd.Column(bd.String(50))
    password = bd.Column(bd.Text)
    img = bd.Column(bd.String(500))

    #constructor
    def __init__(self, nombre, password, img) -> None:
        self.nombre = nombre
        self.password = password
        self.img = img

    #para mostrar el usuario
    def __repr__(self) -> str: #devuelve un string --> str
        return f'Usuario: {self.nombre}'