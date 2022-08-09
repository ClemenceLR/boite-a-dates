from flask import Blueprint, request, jsonify, request,render_template, flash, session
from flask_cors import cross_origin
from passlib.hash import sha256_crypt
from ..data_access.get_datas import get_categories_user,pick_card_user
from ..data_access.insert_datas import insert_card_db, insert_category_db, insert_user_db, check_user_login_unicity
from .auth import login_required

bpapi = Blueprint('api/v1', __name__, url_prefix='/api/v1')

@bpapi.route("/")
def home():
    user_id = check_id_user(session.get("user_id", None))
    categories = get_categories_user(user_id)
    return render_template("home.html", categories = categories, color="#a83246")


@bpapi.route("/categories")
def categories():
    categories = get_categories_user()
    return jsonify(categories)


@bpapi.route("/pick_card")
def pick_card():
    user_id = check_id_user(session.get("user_id", None))
    card = pick_card_user(user_id,-1)
    return render_template("card_presenter.html",card = card)


@bpapi.route("/pick_card_cat/<int:number>", methods=['POST', 'GET'])
def pick_card_cat(number=-1):
    user_id = check_id_user(session.get("user_id", None))
    if request.method == 'POST':
        card = pick_card_user(user_id,number)
        if card == -1:
            flash("Cette catégorie n'a pas de carte !", "error")
            categories = get_categories_user(user_id)
            return render_template("home.html", categories = categories, color="#a83246")
        return render_template("card_presenter.html",card = card)
    else:
        if number != -1:
            card = pick_card_user(user_id,number)
            if card == -1:
                flash("Cette catégorie n'a pas de carte !", "error")
                categories = get_categories_user(user_id)
                return render_template("home.html", categories = categories, color="#a83246")
            else:
                return render_template("card_presenter.html",card = card)


@bpapi.route("/insert_card", methods=["POST", "GET"])
@login_required
def insert_card():
    user_id = check_id_user(session.get("user_id", None))
    if request.method == "POST":
        data = request.form.to_dict()
        card_text = data["card_text"] 
        id_category = int(data["category_list"])
        insert_ret = insert_card_db(user_id, id_category, card_text)
        if insert_ret == -1:
            flash("La création de la carte a échoué", "error")
            return render_template("insert_card.html",  color="#a83246")
        else:
            flash("La carte a été créée", "success")
            categories = get_categories_user(user_id)
            return render_template("home.html", categories = categories, color="#a83246")
    else:
        categories = get_categories_user(user_id)
        return render_template("insert_card.html", categories = categories , color="#a83246")


@bpapi.route("/insert_category", methods=["POST", "GET"])
@login_required
def insert_category():
    user_id = check_id_user(session.get("user_id", None))
    if request.method == "POST":
        data = request.form.to_dict()
        category_name = data["cat_text"] 
        color = data["cat_color"]
        insert_ret = insert_category_db(user_id, category_name,color)
        if insert_ret == -1:
            flash("La catégorie n'a pas pu être créée", "error")
            return render_template("insert_category.html",  color="#a83246")
        elif insert_ret == -2:
            flash("La catégorie existe déjà", "error")
            return render_template("insert_category.html",  color="#a83246")
        else:
            flash("La catégorie a été créée", "success")
            categories = get_categories_user(user_id)
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
            return render_template("home.html", categories = categories, color="#a83246")
        else:
            flash("Ce login existe déjà", "error")
            return render_template("new_user.html", color="#a83246")
    else:
        return render_template("new_user.html", color="#a83246")


def check_id_user(id_to_check):
    if id_to_check == None:
        return 1
    else: 
        return id_to_check