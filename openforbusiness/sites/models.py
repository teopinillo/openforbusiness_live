from django.db import models
from django.forms.models import ModelForm

#US STATES & COUNTIES
#will be filled with an API only once
class States (models.Model):
     name = models.CharField( max_length=100, null=False)
     
     def __str__ (self):
         return self.name
     
#will be filled with an API only once     
class County (models.Model):
    name = models.CharField( max_length=100, null=False)
    state = models.ForeignKey('States', on_delete =  models.CASCADE, related_name="counties")
    
    def __str__(self):
        return self.name
 #will be filled only by admin   
class BusinessClasification (models.Model):
    name = models.CharField (max_length=200, null=False)    
    
    def __str__(self):
        return self.name
    
#will be filled only by admin    
class BusinessIcon (models.Model):
    business = models.ForeignKey ('BusinessClasification',on_delete=models.CASCADE )
    icon = models.ImageField ( null=False, blank=False, upload_to = "business_icons/" )
    
    def __str__(self):
        return self.business.name + ' url: ' + self.icon.url
    
# name, 
#business type
#CATEGORY
#=================FORMS

class BussinesClasificationForm (ModelForm):
    model = BusinessClasification
    fields = '__all__'
    

class BusinessIconForm (ModelForm):
    model = BusinessIcon
    fields = '__all__'