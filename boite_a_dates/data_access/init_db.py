import sqlite3
from os.path import exists

def init_db_script():
    file_exists = exists('./database/boite_a_dates.db')
    if not file_exists:
        with open('./database/boite_a_dates.db', 'w', encoding='utf-8') as f: #creating db file
            create_db = f

        connection = sqlite3.connect('./database/boite_a_dates.db')
        for file in ['script_db.sql', 'insert_data.sql', 'insert_images.sql']:
            with open('./database/' + file) as f: #creating db file
                connection.executescript(f.read())
        connection.commit()
        connection.close()
        print("Database created - loading")
    else :
        print("Database already exists - loading")
