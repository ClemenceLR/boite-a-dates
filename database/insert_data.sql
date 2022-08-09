INSERT INTO "BD_CATEGORIES" ("id_categories","categories_name","color","id_user") VALUES 
(1,"Et si on sortait ?","#32a851",1),
(2,"Coocooning a la maison","#a83246",1),
(3, "Miame","#fac517",1),
(4, "Enfin le Weekend !","#1717fa",1),
(5, "C'est les vacances !","#a338eb",1);


INSERT INTO "BD_USER" ("id_user","login_user","pwd_user" ) VALUES 
(1,"","");


INSERT INTO "BD_CARD" ("id_card","card_text","id_categories", "id_user" ) VALUES 
(1,"Un peu de shopping", 1,1),
(2,"Sortie cinéma",1,1),
(3,"Sortie cinéma à Caen",1,1),
(4,"Sortie cinéma à Centre",1,1),
(5,"Sortie cinéma à Pouet",1,1),
(6,"Câlin gratuit", 2,1),
(7,"Et un ptit épisode un",2,1),
(8,"Soirée gaming", 2,1),
(9,"Soirée gaming deu", 2,1),
(10,"Et 2 ptits épisodes deux",2,1),
(11,"Allons chercher des cookies", 3,1),
(12,"OH LE TACO",3,1),
(13,"Tu prendras bien un ptit Duddy ?",3,1),
(14,"On fait un gateau ?",3,1),
(15,"On fait un pokéball ?",3,1),
(16,"Un petit tour à la mer ?", 4,1),
(17,"Un petit tour en ville ?", 4,1),
(18,"On va à la Fnac ?", 4,1),
(19,"Test", 4,1),
(20,"Test 2", 4,1),
(21, "On plannifie un voyage !",5,1),
(22, "On visite une ville ?",5,1),
(23, "On pars en balade !", 5,1),
(24, "On pars en balade 2!", 5,1),
(25, "On pars en balade 3!", 5,1);