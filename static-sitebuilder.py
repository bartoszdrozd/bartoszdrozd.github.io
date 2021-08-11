import sys
import os
import json
import requests
from geojson import Point, Feature
from flask import Flask, render_template, send_from_directory, redirect, request, session, g, url_for, abort, flash
from flask_frozen import Freezer
from flask_fontawesome import FontAwesome
from dotenv import find_dotenv, load_dotenv
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_mail import Message, Mail

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

FONTAWESOME_SERVE_LOCAL = True 

mail = Mail()
app = Flask(__name__)
app.config.from_object(__name__)
freezer = Freezer(app)
fa = FontAwesome(app)
name="Bartosz Drozd"

app.config.from_envvar('APP_CONFIG_FILE', silent=True)

MAPBOX_ACCESS_KEY = os.environ.get('MAPBOX_ACCESS_KEY')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['WTF_CSRF_SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USE_SSL']=1
app.config["MAIL_USERNAME"] = os.getenv('MAIL_USERNAME')
app.config["MAIL_PASSWORD"] = os.getenv('MAIL_PASSWORD')
app.config["FREEZER_DESTINATION"] = 'docs'
app.config['FONTAWESOME_STYLES'] = ['all']
mail.init_app(app)

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired("Please enter your name.")])
    email = StringField("Email", validators=[Email("Please enter your email address."), DataRequired("Please enter your email address.")])
    subject = TextField("Subject", validators=[DataRequired("Please enter a subject.")])
    message = TextAreaField("Message", validators=[DataRequired("Please enter a message.")])
    submit = SubmitField("Send")

"""@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')"""

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/about/')
def index():
    return render_template('about.html')

@app.route('/my-projects/')
def portfolio():
    return render_template('my-projects.html')

@app.route('/my-resume/')
def resume():
    return render_template('my-resume.html')

@app.route('/my-trips/')
def trips():
    return render_template('mapbox_gl.html', 
        ACCESS_KEY=MAPBOX_ACCESS_KEY)

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
 
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='error.logger.test@gmail.com', recipients=['error.logger.test@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)

            mail.send(msg)

            return render_template('valid-form.html')

    elif request.method == 'GET':
        return render_template('contact.html', form=form)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500




if len(sys.argv) > 1 and sys.argv[1] == "build":
    freezer.freeze()
elif len(sys.argv) > 1 and sys.argv[1] == "debug":
    app.run(debug=True)
elif __name__ == "__main__":
    app.run()
        