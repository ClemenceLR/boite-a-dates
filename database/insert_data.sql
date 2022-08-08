INSERT INTO "BD_CATEGORIES" ("id_categories","categories_name","color","id_user") VALUES 
(1,"Et si on sortait ?","#32a851",1),
(2,"Coocooning a la maison","#a83246",1),
(3, "Miame","#fac517",1),
(4, "Enfin le Weekend !","#1717fa",1),
(5, "C'est les vacances !","#e314d9",1);


INSERT INTO "BD_USER" ("id_user","login_user","pwd_user" ) VALUES 
(1,"","");


INSERT INTO "BD_CARD" ("id_card","card_text","id_categories", "id_user" ) VALUES 
(1,"Un peu de shopping", 1,1),
(2,"Allons chercher des cookies", 3,1),
(3,"Sortie cinéma",1,1),
(4,"Un petit tour à la mer ?", 4,1),
(5,"Calin gratuit", 2,1),
(6,"OH LE TACO",3,1),
(7,"Tu prendras bien un ptit Duddy ?",3,1),
(8,"Et un ptit épisode un",2,1),
(9,"Soirée gaming", 2,1),
(10, "On plannifie un voyage !",5,1),
(11, "On visite une ville ?",5,1),
(12, "On pars en balade !", 1,1);