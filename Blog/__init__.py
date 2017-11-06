from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
  
app = Flask(__name__)
login_manager = LoginManager(app)
Bootstrap(app)


from Blog import views