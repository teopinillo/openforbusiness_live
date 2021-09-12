# ------ SITES APP -----------

from sites.models import BusinessIcon
from django.shortcuts import redirect, render
#from django.contrib.auth.decorators import login_required
from . models import Business, ColorScheme
from django.core.paginator import Paginator


# Create your views here.
def plan_a (request):    
    return render (request,"plan_a.html")

def icons (request):
    business_icons = BusinessIcon.objects.all()
    context = {'business_icons': business_icons}
    
    return render (request,'icons.html', context)

#@login_required
def listed (request):
    all_my_business = ""
    return render (request, 'listed.html')

def index (request):
    all_business = Business.objects.all()
    #    Paginator setup for posts
    paginator = Paginator(all_business, 12)
    page_number = request.GET.get('page')
    business = paginator.get_page(page_number)
    
    context = {"business" : all_business }
    return render (request, 'sites/index.html', context )

def newbusiness (request):
    if request.user.is_authenticated:
        color_schemes = ColorScheme.objects.all()
        context = {"colors" : color_schemes }
        return render (request, 'sites/newbusiness.html', context);
    else:
        return redirect (request, "login")

        
        