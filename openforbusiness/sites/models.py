from django.db import models
from django.forms.models import ModelForm
from users.models import CustomUser
from django.core.validators import RegexValidator

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
    
class Business (ModelForm):
    user = models.ForeignKey ('CustomUser', on_delete=models.CASCADE, related_name="all_business")
    name = models.CharField (max_length=250, null=False, blank=False)
    category = models.ForeignKey ('BusinessClasification', on_delete=models.CASCADE)
    icon = models.ForeignKey ('BusinessIcon', on_delete=models.DO_NOTHING)
    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )

    city = models.CharField(
        "City",
        max_length=1024,
    )
    
    country = models.CharField("Country", max_length=3)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True) # validators should be a list
    email = models.EmailField(max_length = 254)
    #template
    
    website = models.URLField(null=True, blank="True")
    
    image1 = models.ImageField (null=True, upload_to = "business_images/")
    image2 = models.ImageField (null=True, upload_to = "business_images/")
    image3 = models.ImageField (null=True, upload_to = "business_images/")
    
    
    
    def __str__(self):
        return self.category.name + ' ' + self.name

#job_done
# business
# image_job_done
# date

