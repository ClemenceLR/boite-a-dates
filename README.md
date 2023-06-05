# boite-a-dates
This application is a prototype created in order to learn Flask framework.
It allow a user to create / modify cards with date ideas and to pick an idea randomly.

Implemented features:
- User can create an account
- User can log in
- User can create a card
- User can create a card category
- User can edit a card
- User can change the name of a created category
- User can draw a card at random from all categories
- User can draw one or more cards at random from a category

### How to run the programm (on Windows)
1. Install python (https://www.python.org/)
2. Run these commands into the project folder :
```shell
    pip install flask
    pip install virtualenv
    py -m venv env
```
3. Run :
```
    boite_a_dates.bat
```
4. Go to : localhost:5000/api/v1 to access the homepage

Home screen showing all the available categories it is possible to add more if we want: 
![accueil](https://user-images.githubusercontent.com/45121115/223473253-07d79d70-cdf4-4932-8add-d5f75433f850.png)

Print picked cards randomly selected in the category chosen :
![Cartes](https://user-images.githubusercontent.com/45121115/223473445-c4625286-9d14-4905-81a2-315b121bd9ab.png)

---------------------------

Application Boite à Dates
Cette application est un prototype créé dans le but d'apprendre à utiliser le cadriciel Flask.
Elle permet à un utilisateur connecté de créer les cartes avec des idées de rendez vous de sa propre boite et de tirer une carte aléatoire.

Fonctionnalités implémentées :
- L'utilisateur peut créer un compte
- L'utilisateur peut se connecter
- L'utilsateur peut créer une carte
- L'utilisateur peut créer une catégorie de cartes
- L'utilisateur peut modifier une carte
- L'utilisateur peut modifier le nom d'une catégorie créée
- L'utilisateur peut tirer une carte au hasard parmis toutes les catégories
- L'utilisateur peut tirer une ou plusieurs cartes au hasard dans une catégorie


### Comment installer le programme (sur Windows)
1. Installer python (https://www.python.org/)
2. Executer ces commandes dans le répertoire du projet dans un powershell ou une cmd :
```shell
    pip install flask
    pip install virtualenv
    py -m venv env
```
3. Lancer :
```
    boite_a_dates.bat
```
4. Aller à l'adresse : localhost:5000/api/v1 pour accéder à la page d'accueil

Page d'accueil sur laquelle figurent les catégories disponibles, il est possible d'en ajouter de nouvelles : 
![accueil](https://user-images.githubusercontent.com/45121115/223473253-07d79d70-cdf4-4932-8add-d5f75433f850.png)

Afficher les carte tirées dans la catégorie sélectionnée :
![Cartes](https://user-images.githubusercontent.com/45121115/223473445-c4625286-9d14-4905-81a2-315b121bd9ab.png)

