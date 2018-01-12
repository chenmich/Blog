from flask import Flask
from flask.blueprints import Blueprint
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import config

blog_blue = Blueprint('blog', __name__)
db = SQLAlchemy(session_options={"autoflush": False})
login_manager = LoginManager()
bootstrap = Bootstrap()
csrf = CSRFProtect()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(blog_blue, url_prefix='/blog')    

    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)

    return app 

from Blog import views