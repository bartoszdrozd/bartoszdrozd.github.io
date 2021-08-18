import requests
from config import Config
from flask import Flask
from flask_fontawesome import FontAwesome
from flask_mail import Message, Mail


mail = Mail()

app = Flask(__name__)
app.config.from_object(Config)
fa = FontAwesome(app)
mail.init_app(app)

from app import routes