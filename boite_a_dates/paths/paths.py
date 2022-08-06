from flask import Blueprint, request, jsonify, request
from flask_cors import cross_origin
import os 
from ..data_access.get_datas import get_categories_user,pick_card_user

bpapi = Blueprint('api/v1', __name__, url_prefix='/api/v1')

@bpapi.route("/")
def home():
    return jsonify({"status": "UP"})


@bpapi.route("/categories")
def categories():
    categories = get_categories_user()
    return jsonify(categories)

@bpapi.route("/test")
def test():
    test = pick_card_user()
    return jsonify(test)