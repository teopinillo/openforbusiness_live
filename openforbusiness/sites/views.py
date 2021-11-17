# ------ SITES APP -----------
from django.shortcuts import get_object_or_404, redirect, render
#from django.contrib.auth.decorators import login_required
from . models import Business, ColorScheme, PersonFavorite
from . forms import BusinessForm
from django.core.paginator import Paginator
from django.urls import reverse
from users.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

# Create your views here.
def plan_a (request):    
    return render (request,"plan_a.html")

#@login_required
def listed (request):
    all_my_business = Business.objects.filter (owner = request.user)
    context = {"business" : all_my_business }
    return render (request, 'sites/index.html', context)

def index (request):
    Business.objects.filter(favorite=True).update(favorite=False)
    
    #mark user business's favorites
    if request.user.is_authenticated:
        
        favorites = PersonFavorite.objects.filter ( person = request.user)        
        print ("---> favorites 2 <--- ")
        print (favorites)
        for f in favorites.iterator():
            print (f.favorite.name)
            f.favorite.favorite = True
            f.favorite.save()
            
    all_business = Business.objects.all()    
    #    Paginator setup for posts
    paginator = Paginator(all_business, 12)
    page_number = request.GET.get('page')
    business = paginator.get_page(page_number)    
    context = {"business" : all_business }
    return render (request, 'sites/index.html', context )

def myfavorites (request):
    preferred = Business.objects.filter (favorite=True)
    context = {"business" : preferred }
    return render (request, 'sites/index.html', context )

def newbusiness (request):    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BusinessForm (request.POST, request.FILES)
            if form.is_valid():                    
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

@csrf_exempt
@require_http_methods(["POST"])
def setfavorite (request, state, business_id):
    print ("function setfavorite")
    if request.headers.get('x-requested-with') != 'XMLHttpRequest':
        print("delete post function error: no an authentic fetch.")
        return render(request, "sites/404.html")
    
    business = Business.objects.get(pk=business_id)
        
    if business:
        if (state=="true"):
            favorite = PersonFavorite ( person = request.user, favorite = business)            
            favorite.save()                  
        else:
            #retrieve the post object and delete it
            favorite = get_object_or_404 ( PersonFavorite, person = request.user, favorite = business_id)            
            favorite.delete()
        result = {'sucess': 'OK'}
        return JsonResponse(result, status=200)
    else:
       result = {'sucess': 'NOT OK'}
       return JsonResponse(result, status=500) 
        

def reviews (request, business_id):
    business = Business.objects.get(pk=business_id)
    context = {"business": business}
    return render (request, "sites/reviews.html", context)
    
        
        