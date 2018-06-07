from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_migrate import Migrate

from config import Config



app = Flask(__name__)

app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

mail = Mail(app)


from teachersaid import routes, models