CREATE TABLE BD_USER(
        id_user INTEGER NOT NULL,
        login_user VARCHAR (50) NOT NULL,
        pwd_user VARCHAR (50) NOT NULL,
        PRIMARY KEY (id_user)
);

CREATE TABLE BD_CATEGORIES(
        id_categories INTEGER NOT NULL,
        categories_name TEXT NOT NULL,
        color VARCHAR (50) NOT NULL,
        id_user INTEGER NOT NULL,
        PRIMARY KEY (id_categories),
        FOREIGN KEY (id_user) REFERENCES BD_USER(id_user)
);

CREATE TABLE BD_CARD(
        id_card INTEGER NOT NULL,
        card_text TEXT NOT NULL,
        id_categories INTEGER NOT NULL,
        id_user INTEGER NOT NULL,
        PRIMARY KEY (id_card),
        FOREIGN KEY (id_categories) REFERENCES BD_CATEGORIES(id_categories),
        FOREIGN KEY (id_user) REFERENCES BD_USER(id_user)
);