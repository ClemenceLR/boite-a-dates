from .db_access import *
import random


def get_categories_user(id_user=1):
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM BD_CATEGORIES WHERE id_user = ? or id_user = 1",(id_user,))
    categories_liste = []

    for element in cursor.fetchall():
        categories_liste.append({"category":element["categories_name"], "color":element["color"], "id_cat":element["id_categories"]})

    return categories_liste

"""
Return the id of categories available
"""
def get_categories_id(id_user=1):
    cursor = get_db().cursor()
    cursor.execute("SELECT distinct id_categories FROM BD_CARD where id_user=? or id_user = 1",(id_user,))
    categories_valid = []
    for element in cursor.fetchall():
        categories_valid.append(element["id_categories"])

    return categories_valid
"""
Return the string of the category name
"""
def get_category_card(id_category):
    cursor = get_db().cursor()
    cursor.execute("SELECT id_categories,categories_name,color FROM BD_CATEGORIES WHERE id_categories = ?",(id_category,))
    for element in cursor.fetchall():
        return {"id_category": element["id_categories"],"categories_name":element["categories_name"],"color":element["color"]}

"""
Pick a random card in the user cards list
"""
def pick_card_user(id_user=1, id_category=1):
    cursor = get_db().cursor()
    if(id_category == -1):
        available_id = get_categories_id(id_user)
        category_picked = random.choice(available_id)
    else:
        category_picked = id_category
    #print("SELECT card_text FROM BD_CARD where id_user = '%d' and id_categories = '%d'"%(id_user, category_picked))
    cursor.execute("SELECT card_text FROM BD_CARD where (id_user = ? or id_user = 1) and id_categories = ?",(id_user, category_picked))
    cards_pool = []
    for element in cursor.fetchall():
        cards_pool.append({"name":element["card_text"]})
    
    if(len(cards_pool) == 0):
        return -1
    chosen = random.choice(cards_pool)["name"]
    
    category_card = get_category_card(category_picked)

    chosen_card = {
        "category":category_card,
        "card": chosen,
        "color":category_card["color"]
    }
    return chosen_card

"""
Get the user infos by login
"""
def get_user_by_login(user_login):
    cursor = get_db().cursor()
    cursor.execute("SELECT id_user, pwd_user FROM BD_USER WHERE login_user = ?",(user_login,))
    user_data ={}
    for element in cursor.fetchall():
        user_data["id_user"] = element["id_user"]
        user_data["pwd_user"] = element["pwd_user"]
        return user_data

"""
Get the user info by id
"""
def get_user_by_id(user_id):
    cursor = get_db().cursor()
    cursor.execute("SELECT id_user, pwd_user FROM BD_USER WHERE id_user = ?",(user_id,))
    user_data ={}
    for element in cursor.fetchall():
        user_data["id_user"] = element["id_user"]
        user_data["pwd_user"] = element["pwd_user"]
        return user_data

"""
Count the number of cards available
"""
def check_category_cards_total(user_id=1, id_category=1):
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM BD_CARD WHERE (id_user = ? or id_user = 1) and id_categories = ?",(user_id, id_category))
    return len(cursor.fetchall())

"""
Get a set of random cards belonging to a category
"""
def get_random_cards(user_id=1, id_category=1):
    cards_pool = []
    flag = True
    cards_number = check_category_cards_total(user_id, id_category)
    if cards_number > 5:
        cards_number = 5
    for i in range(0, cards_number):
        while flag:
            card = pick_card_user(user_id, id_category)
            if card in cards_pool:
                continue
            else :
                cards_pool.append(card)
                flag = False
        flag = True
    return cards_pool