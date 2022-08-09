import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session)
from werkzeug.security import check_password_hash
from ..data_access.insert_datas import  insert_user_db, check_user_login_unicity
from ..data_access.get_datas import get_categories_user,get_user_by_login, get_user_by_id

from passlib.hash import sha256_crypt

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        data = request.form.to_dict()
        user_login = data["login_text"] #TODO TEST clemence
        user_pwd = data["pwd_text"] 
        if(check_user_login_unicity(user_login) != -2):
            encrypted = sha256_crypt.encrypt(user_pwd)
            id_user = insert_user_db(user_login,encrypted)
            session['user_id'] = id_user
            categories = get_categories_user()
            return render_template("home.html", categories = categories, color="#a83246")
        else:
            flash("Ce nom d'utilisateur existe déjà", "error")
            return render_template("new_user.html", color="#a83246")
    return render_template('new_user.html',color="#a83246")

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        error = None
        data = request.form.to_dict()
        user_login = data["login_text"]
        user_pwd = data["pwd_text"] 
        if user_login == "" and user_pwd == "":
            flash("Login et mots de passe incorrects")
            return render_template('login.html', color="#a83246")
        user = get_user_by_login(user_login)
        if user is None:
            error = "Incorrrect username"
        elif not sha256_crypt.verify(user_pwd,  user['pwd_user'] ):
            error = "Incorrect password"
        if error is None:
            session.clear()
            session['user_id'] = user['id_user']
            flash("Connecté", "success")
            categories = get_categories_user(session['user_id'])
            return render_template("home.html", categories = categories, color="#a83246")
        flash(error)
    return render_template('login.html', color="#a83246")


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_user_by_id(user_id)

@bp.route('/logout')
def logout():
    session.clear()
    return render_template("login.html", color="#a83246")

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return render_template("login.html", color="#a83246")
        return view(**kwargs)
    
    return wrapped_view

    