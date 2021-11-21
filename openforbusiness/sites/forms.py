from django.forms import ModelForm, Textarea
from sites.models import Business,BusinessReview

class BusinessForm (ModelForm):
    class Meta:
        model = Business
        exclude = ['owner']
        
class ReviewForm (ModelForm):
    class Meta:
        model = BusinessReview
        fields = ['comment','score']
        widgets = {
            'comment':Textarea(attrs={'cols':80, 'rows':5}),
        }
        
    
        