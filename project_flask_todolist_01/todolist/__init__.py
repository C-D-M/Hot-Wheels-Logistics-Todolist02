from flask import Flask

# Login
from flask_login import LoginManager, login_manager
from flask_login.utils import login_fresh

# Database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Database
from config import Config

app = Flask(__name__)
# Database
app.config.from_object(Config)

# Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Login
login_manager = LoginManager(app)

# Database - SQLite
with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

from todolist import models, routes