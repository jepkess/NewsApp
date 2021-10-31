from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
#initializing the application
app = Flask(__name__,instance_relative_config = True) #passing in the instance which allow us to connect to the instance folder when the app instance is created.
# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initializing the flask extensions
bootstrap = Bootstrap(app)



from app import views
