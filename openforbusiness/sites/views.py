# ------ SITES APP -----------
from django.shortcuts import redirect, render
#from django.contrib.auth.decorators import login_required
from . models import Business, ColorScheme
from . forms import BusinessForm
from django.core.paginator import Paginator
from django.urls import reverse
from users.models import CustomUser


# Create your views here.
def plan_a (request):    
    return render (request,"plan_a.html")

#@login_required
def listed (request):
    all_my_business = Business.objects.filter (owner = request.user)
    context = {"business" : all_my_business }
    return render (request, 'sites/index.html', context)

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
        if request.method == 'POST':           
            
            #print (request.POST.get("card_image"))
            form = BusinessForm (request.POST, request.FILES) 
            #card_image = request.FILES["card_image"]
            #card_image = request.FILES.get("card_image","hand_shake.jpg")
            #business = Business (owner = request.user, card_image = card_image)      
            #form = BusinessForm ( instance = business, data=request.POST )
            if form.is_valid():
                    #business = form.save(commit=False)   
                    #business.user = request.user
                    #business.save()
                    form.save()
                    return redirect("index")
            else:
                print ("form is not valid!")
                return render (request, 'sites/error.html',{'form':form} )
        else:    
            color_schemes = ColorScheme.objects.all()  
            print ("new business user id: ")
            print( request.user.id )
            form = BusinessForm(initial={'owner' : request.user.id })
            context = {"colors" : color_schemes, 'form': form, }
            #return render (request, 'sites/simple_input.html', context);
            return render (request, 'sites/newbusiness.html', context);
    else:
        return redirect (request, "")

def testcolor (request):
    if request.method=="GET":
        print ("get method")
        color_schemes = ColorScheme.objects.all()
        context = {"colors" : color_schemes}
        return render (request, "sites/testcolor.html", context )
    elif request.method=='POST':
        print ("post method")
        print (request.POST)
        return redirect ( reverse ('index'))
    
def audit (request):
    all_users = CustomUser.objects.all();
    business = Business.objects.all();
    all_data = {"users" : all_users, "business" : business }
    return render (request, "sites/audit.html", all_data)
        
        
        
        