from flask import Blueprint, request, jsonify, request,render_template
from flask_cors import cross_origin
import os 
from ..data_access.get_datas import get_categories_user,pick_card_user

bpapi = Blueprint('api/v1', __name__, url_prefix='/api/v1')

@bpapi.route("/")
def home():
    categories = get_categories_user()
    return render_template("home.html", categories = categories, color="#a83246")


@bpapi.route("/categories")
def categories():
    categories = get_categories_user()
    return jsonify(categories)

@bpapi.route("/pick_card")
def pick_card():
    card = pick_card_user(1,-1)
    return render_template("card_presenter.html",card = card)

@bpapi.route("/pick_card_cat", methods=['POST', 'GET'])
def pick_card_cat():
    if request.method == 'POST':
        request_datas = request.get_json()
        #TODO FORMULAIRE
        card = pick_card_user()
        return render_template("card_presenter.html",card = card)
    else:
        card = pick_card_user()
        return render_template("card_presenter.html",card = card)

@bpapi.route("/test_nav")
def test_nav():
    return render_template("nav.html")