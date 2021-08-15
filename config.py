import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Config(object):
	MAPBOX_ACCESS_KEY = os.environ.get('MAPBOX_ACCESS_KEY')
	app.config.from_envvar('APP_CONFIG_FILE', silent=True)
	app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
	app.config['WTF_CSRF_SECRET_KEY'] = os.getenv('SECRET_KEY')
	app.config['MAIL_SERVER']='smtp.gmail.com'
	app.config['MAIL_PORT']=465
	app.config['MAIL_USE_SSL']=1
	app.config["MAIL_USERNAME"] = os.getenv('MAIL_USERNAME')
	app.config["MAIL_PASSWORD"] = os.getenv('MAIL_PASSWORD')
	app.config['FONTAWESOME_STYLES'] = ['all']
	FONTAWESOME_SERVE_LOCAL = True 
	name = "Bartosz Drozd"