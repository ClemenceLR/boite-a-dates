from .db_access import *
import random


def get_categories_user(id_user=0):
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM BD_CATEGORIES WHERE id_user = '%d' and id_user = 0"%(id_user))
    categories_liste = []

    for element in cursor.fetchall():
        categories_liste.append({"category":element["categories_name"], "color":element["color"]})

    return categories_liste

"""
Return the id of categories available
"""
def get_categories_id(id_user=0):
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM BD_CATEGORIES WHERE id_user = '%d' and id_user = 0"%(id_user))

    categories_id = []
    for element in cursor.fetchall():
        categories_id.append(element["id_categories"])

    return categories_id

"""
Return the string of the category name
"""
def get_category_card(id_category):
    cursor = get_db().cursor()
    cursor.execute("SELECT categories_name,color FROM BD_CATEGORIES WHERE id_categories = '%d'"%(id_category))
    for element in cursor.fetchall():
        return {"categories_name":element["categories_name"],"color":element["color"]}

"""
Pick a random card in the user cards list
"""
def pick_card_user(id_user=0):
    cursor = get_db().cursor()
    available_id = get_categories_id(id_user)
    category_picked = random.choice(available_id)
    cursor.execute("SELECT card_text FROM BD_CARD where id_user = '%d' and id_categories = '%d'"%(id_user, category_picked))

    cards_pool = []
    for element in cursor.fetchall():
        cards_pool.append({"name":element["card_text"]})
    
    category_card = get_category_card(category_picked)

    chosen_card = {
        "category":category_card,
        "card": random.choice(cards_pool)["name"],
        "color":category_card["color"]
    }
    return chosen_card
