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
class Avatar (models.Model):        
    filenumb = models.PositiveIntegerField(default=randint(0, 624))
      
    @property
    def url(self):
        # Return's the full url
        return AVATARS_URL + str(self.filenumb).zfill(4) + ".jpeg"

    def __str__(self):
        return self.url
          
class CustomUser (AbstractUser):
    avatar = models.ForeignKey (Avatar, on_delete = models.DO_NOTHING, null = True, related_name="avatars")
    email = models.EmailField(_('email'), max_length=254, unique=False, null=False, blank=False)
    

    




