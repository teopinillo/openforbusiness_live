from django.forms import ModelForm
from sites.models import Business

class BusinessForm (ModelForm):
    class Meta:
        model = Business
        exclude = ('user',)