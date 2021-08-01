from sites.models import BusinessIcon
from django.shortcuts import render

# Create your views here.
def plan_a (request):    
    return render (request,"plan_a.html")

def icons (request):
    business_icons = BusinessIcon.objects.all()
    context = {'business_icons': business_icons}
    
    return render (request,'icons.html', context)