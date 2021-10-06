from django.db import models
from django.forms.models import ModelForm
from users.models import CustomUser
from django.core.validators import RegexValidator
from django.conf import settings

#will be filled only by admin   
class BusinessClasification (models.Model):
    name = models.CharField (max_length=200, null=False)    
    
    def __str__(self):
        return self.name
    
class BussinesClasificationForm (ModelForm):
    model = BusinessClasification
    fields = '__all__'
    
    
class Business (models.Model):  
    #def __init__(self, user, name, category,address,zip_code,phone_number,email,website,
                 #card_image, facebook, tweeter, instagram, description1, description2, card_style):
        #self.user = user
        #self.name = name
        #self.category = category
        #self.address = address
        #self.zip_code = zip_code
        #self.phone_number = phone_number
        #self.email = email
        #self.webiste = website
        #self.card_image = card_image
        #self.facebook = facebook
        #self.tweeter = tweeter
        #self.instagram = instagram
        #self.description1 = description1 
        #self.description2 = description2
        #self.card_style = card_style
        

    user = models.ForeignKey (settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="all_business")
    name = models.CharField (max_length=250, null=False, blank=False)
    category = models.ForeignKey ('BusinessClasification', on_delete=models.CASCADE)    
    address = models.CharField(max_length=1024,blank=True)
    zip_code = models.CharField(max_length=12, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True) # validators should be a list
    email = models.EmailField(null=True, blank=True, max_length = 254)
    website = models.URLField(null=True, blank="True")    
    card_image = models.ImageField (null=True, blank=True, upload_to = "business_images/")
       
    facebook = models.CharField (null = True, blank=True, max_length = 254)
    tweeter = models.CharField (null = True, blank=True, max_length = 254)
    instagram = models.CharField (null = True, blank=True, max_length = 254)

    description_line_1 = models.CharField (null = True, blank=True, max_length = 254)
    description_line_2 = models.CharField (null = True, blank=True, max_length = 254)
    card_style = models.ForeignKey ('ColorScheme', on_delete=models.CASCADE, related_name="styles")
    
    use_my_card = models.BooleanField ( null = False, default= False)
    my_card = models.ImageField (null=True, blank=True, upload_to = "business_images/")
    
    
    def __str__(self):
        return self.category.name + ' ' + self.name

    def get_facebook_link (self):
        return '<a href = "http://www.facebook.com/' + self.facebook +'">' + self.facebook + '</a>'

    def get_tweeter_link (self):
        return '<a href = "http://www.facebook.com/' + self.facebook +'">' + self.facebook + '</a>'

    def get_instagram_link (self):
        return '<a href = "http://www.facebook.com/' + self.facebook +'">' + self.facebook + '</a>'

    def get_address (self):
        a=""
        if bool(self.address):
            a = self.address
        z=""
        if bool(self.zip_code):
            z = self.zip_code
        return a + z

    def fullData(self):
        return self.name + " " + self.description_line_1 + " "+  self.description_line_2 + " " + self.category + " "+self.address + " "+self.zip_code
                


class ColorScheme (models.Model):
    bck_bottom = models.CharField ( default="white", max_length=8 )
    primary_text = models.CharField ( default="black", max_length=8 )
    back_top = models.CharField ( default="white", max_length=8 )
    icons = models.CharField ( default="black", max_length=8 )
    top_text_secundary = models.CharField ( default="black", max_length=8 )
    name = models.CharField ( null=False, blank=False, unique=True, max_length=20 )
    
    def __str__(self):
        return self.name
    
#job_done
# business
# image_job_done
# date

