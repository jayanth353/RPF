from flask import Flask
from flask_cors import CORS
import os
from main.config import *
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import logging



# Configure the logging format and level
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s in %(module)s : %(message)s')
logFormatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s : %(message)s')

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


