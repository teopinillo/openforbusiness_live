# Project Openforbussines
Capstone project for the CS50 Web Programming with Python and JavaScript

This project will help small bussines to create a web page an a easy way

needs to install crispy_forms
pip install --upgrade django-crispy-forms


development
06/16/2021 Initilizaling the project, creating the users logging pages
06/25/2021 Creating index page
06/27/2021 Creating login/register pages

superuser: teopinillo
pass: entrance9

users: gabriel, akira
pass: entrance
email: @harvard.edu


07/09/2021
 Created the sites app
 designing the first blueprint for sites

 07/24/2021
  Password reset options

08/04/2021
  from django.contrib.auth.decorators import login_required
  @login_requiered
  https://pypi.org/project/django-login-required-middleware/

08/13/2021
error: "GET /accounts/login/?next=/accounts/login/ HTTP/1.1" 302 0
solution: remove, from settings middleware:  
#'login_required.middleware.LoginRequiredMiddleware',


