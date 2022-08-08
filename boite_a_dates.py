#!/bin/env python
import os
from boite_a_dates import create_app
from flask_cors import CORS

from dotenv import load_dotenv
#load_dotenv('.env')

app = create_app(debug=True)

# global to app
#CORS(app, resources={r"/api/v1": {"origins": os.environ.get('CORS_URL')}})
    
if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
