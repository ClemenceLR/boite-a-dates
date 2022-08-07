INSERT INTO "BD_CATEGORIES" ("id_categories","categories_name","color","id_user") VALUES 
(1,"Et si on sortait ?","#32a851",1),
(2,"Coocooning a la maison","#a83246",1),
(3, "Miame","#fac517",1),
(4, "Enfin les vacances ! / Le Weekend !","#1717fa",1);


INSERT INTO "BD_USER" ("id_user","login_user","pwd_user" ) VALUES 
(1,"","");


INSERT INTO "BD_CARD" ("id_card","card_text","id_categories", "id_user" ) VALUES 
(1,"Un peu de shopping", 1,1),
(2,"Bubble tea", 3,1),
(3,"Cinema en centre ville",1,1),
(4,"Un petit tour à la mer ?", 4,1),
(5,"Calin gratuit", 2,1),
(6,"Tacos ?",3,1),
(7,"Un ptit Duddy ?",3,1),
(8,"On continue la serie ?",2,1),
(9,"Soiree gaming", 2,1);