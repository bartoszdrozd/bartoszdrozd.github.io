#import elsa
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
from flask-mail import Message, Mail

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

FONTAWESOME_SERVE_LOCAL = True 

app = Flask(__name__)
app.config.from_object(__name__)
freezer = Freezer(app)
fa = FontAwesome(app)
name="Bartosz Drozd"

app.config.from_envvar('APP_CONFIG_FILE', silent=True)

MAPBOX_ACCESS_KEY = os.environ.get('MAPBOX_ACCESS_KEY')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['WTF_CSRF_SECRET_KEY'] = os.getenv('SECRET_KEY')

app.config["FREEZER_DESTINATION"] = 'docs'
app.config['FONTAWESOME_STYLES'] = ['all']

ROUTE = [
    {"lat": 64.0027441, "long": -22.7066262, "name": "Keflavik Airport", "is_stop_location": True},
    {"lat": 64.0317168, "long": -22.1092311, "name": "Hafnarfjordur", "is_stop_location": True},
    {"lat": 63.99879, "long": -21.18802, "name": "Hveragerdi", "is_stop_location": True},
    {"lat": 63.4194089, "long": -19.0184548, "name": "Vik", "is_stop_location": True},
    {"lat": 63.5302354, "long": -18.8904333, "name": "Thakgil", "is_stop_location": True},
    {"lat": 64.2538507, "long": -15.2222918, "name": "Hofn", "is_stop_location": True},
    {"lat": 64.913435, "long": -14.01951, "is_stop_location": False},
    {"lat": 65.2622588, "long": -14.0179538, "name": "Seydisfjordur", "is_stop_location": True},
    {"lat": 65.2640083, "long": -14.4037548, "name": "Egilsstadir", "is_stop_location": True},
    {"lat": 66.0427545, "long": -17.3624953, "name": "Husavik", "is_stop_location": True},
    {"lat": 65.659786, "long": -20.723364, "is_stop_location": False},
    {"lat": 65.3958953, "long": -20.9580216, "name": "Hvammstangi", "is_stop_location": True},
    {"lat": 65.0722555, "long": -21.9704238, "is_stop_location": False},
    {"lat": 65.0189519, "long": -22.8767959, "is_stop_location": False},
    {"lat": 64.8929619, "long": -23.7260926, "name": "Olafsvik", "is_stop_location": True},
    {"lat": 64.785334, "long": -23.905765, "is_stop_location": False},
    {"lat": 64.174537, "long": -21.6480148, "name": "Mosfellsdalur", "is_stop_location": True},
    {"lat": 64.0792223, "long": -20.7535337, "name": "Minniborgir", "is_stop_location": True},
    {"lat": 64.14586, "long": -21.93955, "name": "Reykjavik", "is_stop_location": True},
]

# Mapbox driving direction API call
ROUTE_URL = "https://api.mapbox.com/directions/v5/mapbox/driving/{0}.json?access_token={1}&overview=full&geometries=geojson"


"""@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')"""

def create_route_url():
    # Create a string with all the geo coordinates
    lat_longs = ";".join(["{0},{1}".format(point["long"], point["lat"]) for point in ROUTE])
    # Create a url with the geo coordinates and access token
    url = ROUTE_URL.format(lat_longs, MAPBOX_ACCESS_KEY)
    return url

def create_stop_location_detail(title, latitude, longitude, index, route_index):
    point = Point([longitude, latitude])
    properties = {
        "title": title,
        'icon': "campsite",
        'marker-color': '#3bb2d0',
        'marker-symbol': index,
        'route_index': route_index
    }
    feature = Feature(geometry = point, properties = properties)
    return feature

def create_stop_locations_details():
    stop_locations = []
    for route_index, location in enumerate(ROUTE):
        if not location["is_stop_location"]:
            continue
        stop_location = create_stop_location_detail(
            location['name'],
            location['lat'],
            location['long'],
            len(stop_locations) + 1,
            route_index
        )
        stop_locations.append(stop_location)
    return stop_locations

def get_route_data():
    # Get the route url
    route_url = create_route_url()
    # Perform a GET request to the route API
    result = requests.get(route_url)
    # Convert the return value to JSON
    data = result.json()

    # Create a geo json object from the routing data
    geometry = data["routes"][0]["geometry"]
    route_data = Feature(geometry = geometry, properties = {})

    return route_data


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired("Please enter your name.")])
    email = StringField("Email", validators=[Email("Please enter your email address."), DataRequired("Please enter your email address.")])
    subject = TextField("Subject", validators=[DataRequired("Please enter a subject.")])
    message = TextAreaField("Message", validators=[DataRequired("Please enter a message.")])
    submit = SubmitField("Send")



# --------------------------- routes (move to another file routes.py)

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
    route_data = get_route_data()
    stop_locations = create_stop_locations_details()
    return render_template('mapbox_gl.html', 
        ACCESS_KEY=MAPBOX_ACCESS_KEY)
    """
        route_data = route_data,
        stop_locations = stop_locations
    )"""

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
 
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            return render_template('valid-form.html')

    elif request.method == 'GET':
        return render_template('contact.html', form=form)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
    
#using elsa to deploy this shit 
"""if __name__ == '__main__':
    from elsa import cli
    cli(app, base_url='https://bartoszdrozd.github.io')"""

if len(sys.argv) > 1 and sys.argv[1] == "build":
    freezer.freeze()
elif sys.argv[1] == "debug":
    app.run(debug=True)

if __name__ == "__main__":
    app.run()
        