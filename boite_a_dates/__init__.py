from flask import Flask
from flask import g
from .data_access.init_db import *
from flask_toastr import Toastr
from flask_login import LoginManager

def create_app(debug=False):
	init_db_script()
	app = Flask(__name__)
	toastr = Toastr(app)
	app.config['SECRET_KEY'] = 'this is a test'
	app.debug = debug

	from .paths import paths
	app.register_blueprint(paths.bpapi)

	from .paths import auth
	app.register_blueprint(auth.bp)
	
	return app