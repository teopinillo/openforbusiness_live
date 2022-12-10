from django.db import models
from django.contrib.auth.models import AbstractUser  
from django.db.models.aggregates import Count
from random import randint  
from django.utils.translation import gettext as _
from appsecrets import AVATARS_URL

"""
avatars are on github, numbered from 000 to nnn 
repository: 
https://github.com/teopinillo/web-resources/tree/main/avatars
"""
        
class CustomUser (AbstractUser):
    avatar = models.IntegerField (default = 1)
    email = models.EmailField(_('email'), max_length=254, unique=False, null=False, blank=False)
    
    def get_avatar_url (self):
        return avatar_url (self.avatar)
    
def avatar_url(id):
        return AVATARS_URL + str(id).zfill(4) + ".jpeg"
