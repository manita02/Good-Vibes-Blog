class Configuracion: 
    DEBUG = True
    TESTING = True

    #Configuración de base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:3306/bd_blog" #se coloca el driver con el cual se conecta a la bd


class Produccion(Configuracion):
    DEBUG = False #sale del modo en desarrollo lo pone en falso


class Desarrollo(Configuracion):
    DEBUG = True
    SECRET_KEY = 'dev'
    TESTING = True
