from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
print(app.config['SECRET_KEY'],"Som3$ec5etK*y" )
csrf = CSRFProtect(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views




