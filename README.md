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

note: postgres should be installed.

```python manage.py makemigrations
python manage.py migrate
python manage.py loaddata BusinessClasification.json
python manage.py loaddata ColorScheme.json```

## check if migrations are ok
`python manage.py migrate --check`

## create a superuser
`python manage.py createsuperuser`

## run the server
`python manage.py runserver`

## go to admin
localhost:8000/admin/

The data was originally dumped with the commands:
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

#### Files and Directories
&#x1f4c2; __/__

&#x1f4c2; openforbusiness
* Pipfile  
* Pipfile.lock  
* README.md  
* requirements.txt  
* &#x1f4c2; static

&#x1f4c2; ./openforbusiness

* appsecrets.py  _keep passwords to login in the database, api key to retrive icons_
* BusinessClasification.json  _data to initilizate the database_
* ColorScheme.json  _data to initilizate the database_
* manage.py  
* &#x1f4c2;media  
* &#x1f4c2;openforbusiness
* &#x1f4c2;sites
* &#x1f4c2;users

&#x1f4c2; ./openforbusiness/openforbusiness

* asgi.py  
* \_\_init__.py  
* settings.py  
* &#x1f4c2; static  
* &#x1f4c2; templates 
* urls.py  
* views.py  
* wsgi.py

&#x1f4c2; ./openforbusiness/openforbusiness/static

* &#x1f4c2; css
* &#x1f4c2; images
* &#x1f4c2; js

&#x1f4c2; ./openforbusiness/openforbusiness/static/css

* loginStyles.css  
* new_business_style.css  
* styles.css

&#x1f4c2; ./openforbusiness/openforbusiness/static/images

* favicon.ico  
* lteo_logo.png

&#x1f4c2; ./openforbusiness/openforbusiness/static/js

* login.js  
* pwdchange.js  
* pwdreset.js  
* signup.js

&#x1f4c2; ./openforbusiness/openforbusiness/templates

&#x1f4c2; openforbusiness

&#x1f4c2; ./openforbusiness/openforbusiness/templates/openforbusiness

* about.html
* contact.html
* layout.html

&#x1f4c2; ./openforbusiness/sites

* admin.py
* forms.py
* &#x1f4c2; migrations
* &#x1f4c2; templates
* urls.py
* apps.py
* \_\_init__.py
* models.py
* static
* tests.py
* views.py

&#x1f4c2; ./openforbusiness/sites/migrations

 _Contain all project’s migrations_


&#x1f4c2; ./openforbusiness/sites/static

* &#x1f4c2; images
* &#x1f4c2; js

&#x1f4c2; ./openforbusiness/sites/static/images

* hand_shake.jpg

&#x1f4c2; ./openforbusiness/sites/static/js

* newbusiness.js  	_instant change html page to see results as information is entered._
* newreview.js  	_Track when user click on the star review_
* sites.js			_Allow rating, flipping the card, set favorite_

&#x1f4c2; ./openforbusiness/sites/templates

&#x1f4c2; sites

&#x1f4c2; ./openforbusiness/sites/templates/sites

* audit.html     
* card.html _card template_
* index.html   _home page_
* newbusiness.html  _creating new business page_
* pagination.html   	&#x1f4cc;_django pagination, html fragment to be included in index html_
* reviews.html  _reiews page_
* cardback.html  _back of the card_
* error.html  _error page_
* icons.html
* listed.html _page for user's business listed_
* new_review.html   _adding a new review_
* previewcard.html  _the card that is displayed when enter a new business_
* schemes.html _page that display all card layouts_

&#x1f4c2; ./openforbusiness/users:

* admin.py  
* apps.py  
* forms.py  
* \_\_init\_\_.py  
* &#x1f4c2; migrations  
* models.py  
* &#x1f4c2; static  
* &#x1f4c2; templates  
* tests.py  
* urls.py  
* views.py

&#x1f4c2; ./openforbusiness/users/migrations

&#x1f4c2; ./openforbusiness/users/static

&#x1f4c2; ./openforbusiness/users/templates

* &#x1f4c2; registration

* &#x1f4c2; users

&#x1f4c2; ./openforbusiness/users/templates/registration

* login.html  
* password_change_done.html  
* password_change_form.html  
* password_reset_done.html  
* password_reset_form.html

&#x1f4c2; ./openforbusiness/users/templates/users

* avatars.html  
* profile.html  
* signup.html

&#x1f4c2; ./static

* &#x1f4c2; admin
* &#x1f4c2; css
* &#x1f4c2; images
* &#x1f4c2; js

&#x1f4c2; ./static/admin _django default directory_

* &#x1f4c2; css		
* &#x1f4c2; fonts		
* &#x1f4c2; img
* &#x1f4c2; js

&#x1f4c2; ./static/css

* loginStyles.css
* new_business_style.css  
* styles.css

&#x1f4c2; ./static/images

* favicon.ico
* hand_shake.jpg
* &#x1f4c2; images
* lteo_logo.png
* photo-camera.png

&#x1f4c2; ./static/images/images &#x1f4cc; _In this directory django keep the images upload to the site_


&#x1f4c2; ./static/js

* login.js  
* newbusiness.js  
* newreview.js
* pwdchange.js
* pwdreset.js  
* signup.js
* sites.js


teopinillo Dec, 2021




















 

  