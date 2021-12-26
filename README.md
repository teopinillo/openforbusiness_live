# Project OpenForBusiness
Capstone project for the CS50 Web Programming with Python and JavaScript
https://cs50.harvard.edu/web/2020/projects/final/capstone/

The intention of this project is to help small bussines to create an online presentation card.
Also, customers can write and rate the business to help others future customers
which business to select.



### Python's Package needed to run this project.

The file requirement.txt contains all necesary packages. Among them **pillow**, and **crispy forms**.
To install the packages: *$[ pipenv install](https://pipenv-fork.readthedocs.io/en/latest/basics.html " pipenv install")*

## Initializing the Database.
The project needs to initialize two tables before starting.

python manage.py loaddata BusinessClasification.json
python manage.py loaddata ColorScheme.json

The data was originallu dumped with the commands:
python manage.py dumpdata sites.BusinessClasification > BusinessClasification.json
python manage.py dumpdata sites.ColorScheme > ColorScheme.json

------------

## App Users
Keep all referent to user register, login, logout, pasword changes and recovery.

## App Sites
The main part of the project. Keep the logic for the cards.

For this project is used Postgree as a database.

#### Models Description
**BusinessClasification** : Hold the possibles clasification for a business.
**Business** Hold the information related to a business.
**PersonFavorite** : Track the user favorites business.
**ColorScheme** : Color Scheme for business's card.
  
  Color scheme used: 
  https://www.w3schools.com/colors/colors_schemes.asp
  color names given by:
  https://chir.ag/projects/name-that-color
  
**BusinessReview** : Keep reviews for business made by users.

#### Other resources used:
  Font Awesome 4.  https://fontawesome.com/v4.7/icons/
  Flaticon https://www.flaticon.com/
  Markup Editor https://markdown-editor.github.io/


teopinillo Dec, 2021




















 

  