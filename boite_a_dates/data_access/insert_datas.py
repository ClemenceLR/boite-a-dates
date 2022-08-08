from .db_access import *

def insert_card_db(id_user, id_category, card_text):
    try:
        cursor = get_db().cursor()
        cursor.execute("INSERT INTO BD_CARD (card_text,id_categories,id_user) VALUES ('%s',%d,%d)"%(card_text,id_category,id_user))
        get_db().commit()
    except Exception:
        return -1

def insert_category(id_user, category_name,color):
    cursor = get_db().cursor()
    cursor.execute("INSERT INTO BD_CATEGORIES (categories_name,color,id_user) VALUES ('%s','%s',%d)"%(category_name,color,id_user))
    get_db().commit()


def insert_user(login_user, pwd_user):
    cursor = get_db().cursor()
    cursor.execute("INSERT INTO BD_USER (login_user,pwd_user) VALUES ('%s','%s')"%(login_user,pwd_user))
    get_db().commit()
