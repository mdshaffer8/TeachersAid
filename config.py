import os
from os.path import join, isfile
from werkzeug.utils import secure_filename

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    
    # UPLOAD_FOLDER = '/static/img'
    # ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    UPLOADS_DEFAULT_DEST = basedir + '/teachersaid/static/img/'
    UPLOADS_DEFAULT_URL = 'http://localhost:5000/static/img/'
 
    UPLOADED_IMAGES_DEST = basedir + '/teachersaid/static/img/'
    UPLOADED_IMAGES_URL = 'http://localhost:5000/static/img/'