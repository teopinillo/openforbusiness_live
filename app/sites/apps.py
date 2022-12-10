from django.apps import AppConfig

class SitesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sites'
    
    def ready(self):
        print ("sites application started")
        pass #start up code start here
