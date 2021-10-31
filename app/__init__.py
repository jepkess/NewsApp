# from flask import Flask
# from config import DevConfig
# from flask_bootstrap import Bootstrap
# from config import config_options
# #initializing the application
# app = Flask(__name__,instance_relative_config = True) #passing in the instance which allow us to connect to the instance folder when the app instance is created.
# # Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# #initializing the flask extensions
# bootstrap = Bootstrap(app)



# from app import views
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app
