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
        if request.method == 'POST':
            #print (request.POST)            
            #name = request.POST.get('name')            
            #description_line_1 = request.POST.get('description1')
            #description_line2_ = request.POST.get('description2')
            #card_style = request.POST.get('card_style')
            #address = request.POST.get('address')
            #zip = request.POST.get('zip')
            #phone = request.POST.get('phone')
            #webiste=request.POST.get('website')
            #facebook = request.POST.get('facebook')
            #instagram = request.POST.get('instagram')
            #tweeter = request.POST.get('tweeter')
                                #user, name, category, address,z ip_code, phone_number, email, website, card_image, facebook, tweeter, instagram, description1, description2, card_style):
            #business = Business (user, name, category, address, zip_code, phone_number, email, website, card_image, facebook, tweeter, instagram, description1, description2, card_style)
            #business.save()
            #print (request.POST)
            #print (request.POST.get("card_image"))
            
            #business = Business (user = request.user)
            form = BusinessForm (request.POST, request.FILES)            
            if form.is_valid():
                    business = form.save(commit=False)   
                    business.user = request.user
                    business.save()
                    return redirect("index")
            else:
                print ("form is not valid!")
                return render (request, 'sites/error.html',{'form':form} )
        else:    
            color_schemes = ColorScheme.objects.all()  
            form = BusinessForm()
            context = {"colors" : color_schemes, 'form': form, }
            #return render (request, 'sites/simple_input.html', context);
            return render (request, 'sites/newbusiness.html', context);
    else:
        return redirect (request, "login")

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
        
        
        
        