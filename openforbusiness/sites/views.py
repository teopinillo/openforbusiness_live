from sites.models import BusinessIcon
from django.shortcuts import render
#from django.contrib.auth.decorators import login_required

# Create your views here.
def plan_a (request):    
    return render (request,"plan_a.html")

def icons (request):
    business_icons = BusinessIcon.objects.all()
    context = {'business_icons': business_icons}
    
    return render (request,'icons.html', context)

#@login_required
def my_business (request):
    all_my_business = ""
    return render (request, 'mybusiness.html')