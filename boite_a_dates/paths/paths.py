from flask import Blueprint, request, jsonify, request,render_template, flash
from flask_cors import cross_origin
from passlib.hash import sha256_crypt
import os 
from ..data_access.get_datas import get_categories_user,pick_card_user
from ..data_access.insert_datas import insert_card_db, insert_category_db, insert_user_db, check_user_login_unicity

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

@bpapi.route("/pick_card_cat/<int:number>", methods=['POST', 'GET'])
def pick_card_cat(number=-1):
    if request.method == 'POST':
        request_datas = request.get_json()
        #TODO FORMULAIRE
        card = pick_card_user(1,number)
        if card == -1:
            flash("This category has no cards", "error")
            categories = get_categories_user()
            return render_template("home.html", categories = categories, color="#a83246")

        return render_template("card_presenter.html",card = card)
    else:
        if number != -1:
            card = pick_card_user(1,number)
            if card == -1:
                flash("This category has no cards", "error")
                categories = get_categories_user()
                return render_template("home.html", categories = categories, color="#a83246")
            else:
                return render_template("card_presenter.html",card = card)

@bpapi.route("/test_nav")
def test_nav():
    return render_template("nav.html")

@bpapi.route("/insert_card", methods=["POST", "GET"])
def insert_card():
    if request.method == "POST":
        data = request.form.to_dict()
        card_text = data["card_text"] 
        id_user = 1
        id_category = int(data["category_list"])

        insert_ret = insert_card_db(id_user, id_category, card_text)
        if insert_ret == -1:
            flash("Card creation failed", "error")
        
        flash("Card was created", "success")
        categories = get_categories_user()
        return render_template("home.html", categories = categories, color="#a83246")
    else:
        id_user = 1
        categories = get_categories_user(id_user)
        print(categories)
        return render_template("insert_card.html", categories = categories , color="#a83246")

@bpapi.route("/insert_category", methods=["POST", "GET"])
def insert_category():
    if request.method == "POST":
        data = request.form.to_dict()
        category_name = data["cat_text"] 
        color = data["cat_color"]
        id_user = 1
        print(category_name)
        print(color)

        insert_ret = insert_category_db(id_user, category_name,color)
        if insert_ret == -1:
            flash("Category creation failed", "error")
        
        flash("Category was created", "success")
        categories = get_categories_user()
        return render_template("home.html", categories = categories, color="#a83246")
    else:
        return render_template("insert_category.html", color="#a83246")

@bpapi.route("/create_user", methods=["GET","POST"])
def create_user():
    if request.method == "POST":
        data = request.form.to_dict()
        user_login = data["login_text"] #TODO TEST clemence
        user_pwd = data["pwd_text"] 
        if(check_user_login_unicity(user_login) != -2):
            encrypted = sha256_crypt.encrypt(user_pwd)
            insert_user_db(user_login,encrypted)
            categories = get_categories_user()
            print("success")
            return render_template("home.html", categories = categories, color="#a83246")
        else:
            print("failed")
            flash("This login already exists", "error")
            return render_template("new_user.html", color="#a83246")
    else:
        return render_template("new_user.html", color="#a83246")

@bpapi.route("/login")
def log_user():
    user_login = "clemence"
    user_pwd = "clemence"
    encrypted = get_user_by_login()