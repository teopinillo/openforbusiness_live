# Project OpenForBusiness
Capstone project for the CS50 Web Programming with Python and JavaScript
https://cs50.harvard.edu/web/2020/projects/final/capstone/

The intention of this project is to help small bussines to create an online presentation card.
Also, customers can write and rate the business to help others future customers
which business to select.

You can clone this branch with the command:
`git clone -b web50/projects/2020/x/capstone https://github.com/me50/teopinillo.git`

### Install the packages according to the configuration file **requirements.txt

`pip install -r requirements.txt`

For this project is used Postgree as a database. We need to create the database 'ofbdb'

The file requirement.txt contains all necesary packages. Among them **pillow**, and **crispy forms**.
## The appsecret file
You must create this file on the root directory of the application.
/openforbusiness/appsecrets.py

the file should contains the following:

```
DATABASE_NAME = 'ofbdb'
DATABASE_ADMIN_PASSWORD = 'your admin password for the database'
SECRET_KEY = 'a secret key that will be used to create hashes'

#GITHHUB ULR FOR AVATARS
AVATARS_URL = "https://raw.githubusercontent.com/teopinillo/web-resources/main/avatars/"
AVATARS_TOTAL = 650

APP_LOGO_URL = "https://dl.dropboxusercontent.com/s/0omlfeix9bt9s2j/dog-5952028_640.jpg?dl=0"

MY_EMAIL="your_email"
MY_EMAIL_PASSWORD="your_email_passowrd"
```

## Initializing the Database.
The project needs to initialize two tables before starting.

note: postgres should be installed.

```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata BusinessClasification.json
python manage.py loaddata ColorScheme.json
```

## check if migrations are ok
`python manage.py migrate --check`

## create a superuser
`python manage.py createsuperuser`

## run the server
`python manage.py runserver`

## go to admin
localhost:8000/admin/

The data was originally dumped with the commands:

`python manage.py dumpdata sites.BusinessClasification > BusinessClasification.json`

`python manage.py dumpdata sites.ColorScheme > ColorScheme.json`

------------

## App Users
Keep all referent to user register, login, logout, pasword changes and recovery.

## App Sites
The main part of the project. Keep the logic for the cards.

#### Models Description

**BusinessClasification** : Hold the possibles clasification for a business.

**Business** Hold the information related to a business.

**PersonFavorite** : Track the user favorites business.

**ColorScheme** : Color Scheme for business's card.

**BusinessReview** : Keep reviews for business made by users.
  
  #### Color scheme used 
  https://www.w3schools.com/colors/colors_schemes.asp

  #### Color names given by:
  https://chir.ag/projects/name-that-color

#### Other resources used:

  ##### Font Awesome 4.  https://fontawesome.com/v4.7/icons/

  ##### Flaticon https://www.flaticon.com/

  ##### Markup Editor https://markdown-editor.github.io/

## Files and Directories

&#x1f4c2; openforbusiness
  * &#x1f4c2; openforbusiness
    * &#x1f4c2; static 
      * &#x1f4c2; css
        * &#x1f3a8;loginStyles.css  _style sheet for the login page_
        * &#x1f3a8;new_business_style.css  _style sheet for new business page_
        * &#x1f3a8;styles.css _general style across diferent project web page_
      * &#x1f4c2; images
        * favicon.ico  _favicon icon_
        * lteo_logo.png _my logo_
      * &#x1f4c2; js
        * login.js  _set properties to elements on the login html page_
        * pwdchange.js  _set properties to elements on password change html page_
        * pwdreset.js  _set properties to the elements on the password reset html page_
        * signup.js _set properties to elements on signup html page_
    * &#x1f4c2; templates
      * &#x1f4c2; openforbusiness
        * &#x1f30d;about.html _about page_
        * &#x1f30d;contact.htmln _contact page_
        * &#x1f30d;layout.html _general layout used across all pages_
    * &#x1f40d; \_init\_.py
    * &#x1f40d; asgi.py  _Django ASGI_
    * &#x1f40d; settings.py _app settings_
    * &#x1f40d; urls.py  _app urls_
    * &#x1f40d; views.py  _app views_
    * &#x1f40d; wsgi.py _Web Server Interface. Python Standard_
  * &#x1f40d;appsecrets.py  _keep passwords to login in the database, api key to retrive icons_
  * BusinessClasification.json  _data to initilizate the database_
  * ColorScheme.json  _data to initilizate the database_
  * manage.py  
  * &#x1f4c2;media  
  * &#x1f4c2;openforbusiness
  * &#x1f4c2;sites
    * &#x1f4c2; migrations _Contains all project’s migrations_
    * &#x1f4c2; static
      * &#x1f4c2; images
        * hand_shake.jpg
      * &#x1f4c2; js
        * newbusiness.js  	_instantly change the HTML page to see results as information is entered._
        * newreview.js  	_Track when user click on the star review_
        * sites.js			_Allow rating, flipping the card, set favorite_
    * &#x1f4c2; templates
      * &#x1f4c2; sites
        * &#x1f30d;audit.html _just for testing. We can see all data entered_
        * &#x1f30d;card.html _card template_
        * &#x1f30d;index.html   _home page_
        * &#x1f30d;newbusiness.html  _creating new business page_
        * &#x1f30d;pagination.html   _django pagination, html fragment to be included in index html_
        * &#x1f30d;reviews.html  _reiews page_
        * &#x1f30d;cardback.html  _back of the card page_
        * &#x1f30d;error.html  _error page_
        * &#x1f30d;icons.html _icons page_
        * &#x1f30d;listed.html _page for user's business listed_
        * &#x1f30d;new_review.html   _adding a new review_
        * &#x1f30d;previewcard.html  _the card that is displayed when enter a new business_
        * &#x1f30d;schemes.html _page that display all card layouts_
    * &#x1f40d; \_init\_.py _tells python this directory contains packages_
    * &#x1f40d; admin.py _Django admin site_
    * &#x1f40d; apps.py _application configuration_
    * &#x1f40d; forms.py _Django forms_
    * &#x1f40d; models.py _Data Structure_
    * &#x1f40d; tests.py _Test Logic_
    * &#x1f40d; urls.py _urls for the site app_
    * &#x1f40d; views.py _django views for the site app_
  * &#x1f4c2;users  
    * &#x1f4c2; migrations _django migrations_
    * &#x1f4c2; templates
      * &#x1f4c2; registration 
        * &#x1f30d;login.html  _login page_
        * &#x1f30d;password_change_done.html  _password change done page_
        * &#x1f30d;password_change_form.html  _page to change the user password_
        * &#x1f30d;password_reset_done.html  _page when the password reset pass ok_
        * &#x1f30d;password_reset_form.html _page to reset the password_
      * &#x1f4c2; users      
        * &#x1f30d;avatars.html  _page to change the user avatar_
        * &#x1f30d;profile.html  _user profile page_
        * &#x1f30d;signup.html  _sign up page for new users_
    * &#x1f40d; \_init\_.py
    * &#x1f40d;admin.py  
    * &#x1f40d;apps.py  _user app configuration_
    * &#x1f40d;forms.py _user app django forms_
    * &#x1f40d;models.py _data models for users_
    * &#x1f40d;tests.py  _test module_
    * &#x1f40d;urls.py  _user app urls_
    * &#x1f40d;views.py _user app views_
* &#x1f4c2; static
  * &#x1f4c2; admin _created by Django by default. Is the admin page_
    * &#x1f4c2; css		
    * &#x1f4c2; fonts		
    * &#x1f4c2; img    
  * &#x1f4c2; images _directory for card's presentation images._
    * &#x1f4c2; images _In this directory django keep the images upload to the site_
  * &#x1f4c2; js
* .gitignore _file to ignore for Git_
* Pipfile  _dedicated file used by the Pipenv virtual environment to manage project dependencies. This file is essential for using Pipenv. When you create a Pipenv environment either for a new or an existing project, the Pipfile is generated automatically._
* Pipfile.lock  _Has the specific versions for each dependency._
* README.md   _this file_
* requirements.txt  _list all the dependencies for the project_

teopi Oct, 2022




















 

  