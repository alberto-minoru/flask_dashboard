import os


class Config:
    CSRF_ENABLE = True
    SECRET = os.getenv('SECRET')
    if SECRET is None:
        SECRET = '123456'
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_FOLDER = os.path.join(ROOT_DIR, 'templates')
    APP = None
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    if SQLALCHEMY_DATABASE_URI is None:
        SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://teste:teste=@localhost:3306/flask_dashboard'


class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8080
    URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST)


class ProductionConfig(Config):
    DEBUG = False
    IP_HOST = 'localhost'
    PORT_HOST = 80
    URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST)


app_config = {
    'development': DevelopmentConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')
if app_active is None:
    app_active = 'development'
