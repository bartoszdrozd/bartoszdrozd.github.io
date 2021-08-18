import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Config(object):
	MAPBOX_ACCESS_KEY = os.environ.get('MAPBOX_ACCESS_KEY')
	SECRET_KEY = os.environ.get('SECRET_KEY')
	WTF_CSRF_SECRET_KEY = os.getenv('SECRET_KEY')
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 465
	MAIL_USE_SSL = 1
	MAIL_USERNAME = os.getenv('MAIL_USERNAME')
	MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
	FONTAWESOME_STYLES = ['all']
	FONTAWESOME_SERVE_LOCAL = True 
	name = "Bartosz Drozd"