import sys
import os
#import elsa

from flask import Flask, render_template, send_from_directory, redirect
from flask_frozen import Freezer
from flask_fontawesome import FontAwesome

FONTAWESOME_SERVE_LOCAL = True 


app = Flask(__name__)
app.config.from_object(__name__)
freezer = Freezer(app)
fa = FontAwesome(app)
name="Bartosz Drozd"

app.config["FREEZER_DESTINATION"] = 'docs'
app.config['FONTAWESOME_STYLES'] = ['brands']

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
    return render_template('my-trips.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#using elsa to deploy this shit 
"""if __name__ == '__main__':
    from elsa import cli
    cli(app, base_url='https://bartoszdrozd.github.io')"""

if len(sys.argv) > 1 and sys.argv[1] == "build":
    freezer.freeze()
else:
    app.run() # for development (debug=True, port=8000)
        