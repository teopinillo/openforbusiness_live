from django.db import models
from django.forms.models import ModelForm
from users.models import CustomUser
from django.core.validators import RegexValidator
from django.conf import settings
from datetime import datetime
from django.db.models import Avg

#will be filled only by admin   
class BusinessClasification (models.Model):
    name = models.CharField (max_length=200, null=False)    
    
    def __str__(self):
        return self.name
    
class BussinesClasificationForm (ModelForm):
    model = BusinessClasification
    fields = '__all__'
    
    
class Business (models.Model):  
    owner = models.ForeignKey (settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="all_business")
    name = models.CharField (max_length=50, null=False, blank=False)
    category = models.ForeignKey ('BusinessClasification', on_delete=models.CASCADE, default = 1)    
    address = models.CharField(max_length=1024,blank=True)
    zip_code = models.CharField(max_length=12, null=True, blank=True)
    phone_1 = models.CharField(max_length=15, blank=True) # validators should be a list
    phone_2 = models.CharField(max_length=15, blank=True) # validators should be a list
    email = models.EmailField(null=True, blank=True, max_length = 254)
    website = models.URLField(null=True, blank="True")    
    card_image = models.ImageField (null=True, blank=True, upload_to = "images/", default="hand_shake.jpg")
       
    facebook = models.CharField (null = True, blank=True, max_length = 254)
    twitter = models.CharField (null = True, blank=True, max_length = 254)
    instagram = models.CharField (null = True, blank=True, max_length = 254)

    services_1 = models.CharField (null = True, blank=True, max_length = 50)
    services_2 = models.CharField (null = True, blank=True, max_length = 50)
    services_3 = models.CharField (null = True, blank=True, max_length = 50)
    services_4 = models.CharField (null = True, blank=True, max_length = 50)
    
    card_style = models.ForeignKey ('ColorScheme', on_delete=models.CASCADE, related_name="styles")    
    use_my_card = models.BooleanField ( null = False, default= False)
    my_card = models.ImageField (null=True, blank=True, upload_to = "images/" )
    rating = models.IntegerField (null=True, blank=True, default=0)
    #this is a temp filed, used as s flag, for the index view.
    #we get all the business that has been saved as favorite and filtered by the
    #current user.
    favorite = models.BooleanField (default=False)
        
    def __str__(self):
        return self.name

    def get_address (self):
        a=""
        if bool(self.address):
            a = self.address
        z=""
        if bool(self.zip_code):
            z =" " + self.zip_code
        return a + z

    def get_rating (self):
        avg = self.b_reviews.all().aggregate(Avg('score')).get('score__avg')
        if (avg):
            return avg
        return 0
    
    def getMaxStars(self):
        return range(1, 6);    
    
    def fullData(self):
        return self.name + " " + self.description_line_1 + " "+  self.description_line_2 + " " + self.category + " "+self.address + " "+self.zip_code
    
    def getName(self):
        return self.name
    
    def reviews_total(self):
        total = self.b_reviews.count()
        return total
    
    
    #function used for search. It willcreate an string with all words in the business model    
    def getWords (self):
        def formatWord (w):
            if (w is not None):
                return (str(w) + " ").upper()
            else:
                return ""
        
        return  formatWord (self.name) +\
                formatWord (self.category.name) +\
                formatWord (self.address) +\
                formatWord (self.zip_code) +\
                formatWord (self.phone_1) +\
                formatWord (self.phone_2)  +\
                formatWord (self.email)  +\
                formatWord (self.website)  +\
                formatWord (self.facebook) +\
                formatWord (self.tweeter) +\
                formatWord (self.instagram) +\
                formatWord (self.services_1) +\
                formatWord (self.services_2) +\
                formatWord (self.services_3) + \
                formatWord (self.services_4)
    
#track the user favorite business
class PersonFavorite (models.Model):
    person = models.ForeignKey (settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "preferred_business")
    favorite = models.ForeignKey (Business, on_delete = models.CASCADE, related_name = "liked_by_users");
 
#Color schemes for cards  
class ColorScheme (models.Model):    
    bg_center = models.CharField ( default="white", max_length=8 )
    txt_bottom = models.CharField ( default="#000000", max_length=8 )
    bg_top = models.CharField ( default="white", max_length=8 )
    icons = models.CharField ( default="#000000", max_length=8 )
    txt_top = models.CharField ( default="black", max_length=8 )
    txt_center = models.CharField ( default="#000000", max_length=8 )
    bg_bottom = models.CharField ( default="#FFFFFF", max_length=8 )
    
    name = models.CharField ( null=False, blank=False, unique=True, max_length=20 )
    
    def __str__(self):
        return self.name
    
    
    
#job_done
# businesss
# image_job_done
# date
SCORE_CHOICES = [
    ( 1,"*"),
    ( 2,"**"),
    ( 3,"***"),
    ( 4,"****"),
    ( 5,"*****")
    ]

class BusinessReview(models.Model):
    person = models.ForeignKey (settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    review_for = models.ForeignKey (Business, on_delete = models.CASCADE, related_name="b_reviews");
    comment = models.CharField (null=False, blank=False, max_length = 255)
    date = models.DateField (default=datetime.today)
    score = models.IntegerField(default=0, choices=SCORE_CHOICES)
    
    def __str__(self):
        return self.review_for.name +" "+ str(self.score) + " "+ self.comment
    
    def rating(self):
        rate="Terrible"
        if self.score == 5:
            rate="Excellent"
        elif self.score == 4:
            rate="Vey Good"
        elif self.score == 3:
            rate="Average"
        elif self.score == 2:
            rate="Poor"        
        return rate

