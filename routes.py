from app import app
from flask import render_template, request, flash, send_from_directory
from flask_mail import Message
from app.forms import ContactForm
from config import Config
import os

MAPBOX_ACCESS_KEY = os.environ.get('MAPBOX_ACCESS_KEY')

# Get mail instance from app
from app import mail

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'img'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

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
    return render_template('my-trips.html')

@app.route('/eurotrip18/')
def trip18():
    return render_template('eurotrip18.html',
        ACCESS_KEY=MAPBOX_ACCESS_KEY)

@app.route('/eurotrip19/')
def trip19():
    return render_template('eurotrip19.html',
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