import sys
import os
import json
import requests
from config import Config
from geojson import Point, Feature
from flask import Flask, render_template, send_from_directory, redirect, request, session, g, url_for, abort, flash
from flask_fontawesome import FontAwesome
from dotenv import find_dotenv, load_dotenv
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_mail import Message, Mail


mail = Mail()

app = Flask(__name__)
app.config.from_object(Config)
fa = FontAwesome(app)
mail.init_app(app)

from app import routes

if __name__ == "__main__":
    app.run()
        