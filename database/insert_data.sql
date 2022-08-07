INSERT INTO "BD_CATEGORIES" ("id_categories","categories_name","color","id_user") VALUES 
(1,"Et si on sortait ?","#32a850",0),
(2,"Coocooning a la maison","#a83246",0),
(3, "Miame","#fac507",0),
(4, "Enfin les vacances ! / Le Weekend !","#0717fa",0);


INSERT INTO "BD_USER" ("id_user","login_user","pwd_user" ) VALUES 
(0,"","");


INSERT INTO "BD_CARD" ("id_card","card_text","id_categories", "id_user" ) VALUES 
(0,"Un peu de shopping", 1,0),
(1,"Bubble tea", 3,0),
(2,"Cinema en centre ville",1,0),
(3,"Un petit tour à la mer ?", 4,0),
(4,"Calin gratuit", 2,0),
(5,"Tacos ?",3,0),
(6,"Un ptit Duddy ?",3,0),
(7,"On continue la série ?",2,0),
(8,"Soiree gaming", 2,0);