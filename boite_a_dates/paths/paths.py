from flask import Blueprint, request, jsonify, request
from flask_cors import cross_origin
import os 

bpapi = Blueprint('api/v1', __name__, url_prefix='/api/v1')

@bpapi.route("/")
def home():
    return jsonify({"status": "UP"})
