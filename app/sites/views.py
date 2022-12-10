# ------ SITES APP -----------
from django.shortcuts import get_object_or_404, redirect, render
#from django.contrib.auth.decorators import login_required
from . models import Business, ColorScheme, PersonFavorite, BusinessReview
from . forms import BusinessForm, ReviewForm
from django.core.paginator import Paginator
from django.urls import reverse
from users.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

#@login_required
def listed (request):
    all_my_business = Business.objects.filter (owner = request.user)
    context = {"business" : all_my_business, "editable" : True }
    return render (request, 'sites/index.html', context)

def index (request):
    Business.objects.filter(favorite=True).update(favorite=False)
    
    #mark user business's favorites
    if request.user.is_authenticated:        
        favorites = PersonFavorite.objects.filter ( person = request.user)
        for f in favorites.iterator():            
            f.favorite.favorite = True
            f.favorite.save()
            
    all_business = Business.objects.all()    
    #Paginator
    paginator = Paginator(all_business, 9)
    page_number = request.GET.get('page')
    business = paginator.get_page(page_number)    
    context = {"business" : business, "editable": False }
    return render (request, 'sites/index.html', context )

def myfavorites (request):
    preferred = Business.objects.filter (favorite=True)
    context = {"business" : preferred }
    return render (request, 'sites/index.html', context )

def newbusiness (request):   
    color_schemes = ColorScheme.objects.all()
    form = BusinessForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            business = Business(owner=request.user)
            form = BusinessForm (request.POST, request.FILES, instance=business)
            if form.is_valid():                    
                    form.save()
                    return redirect("index")            
        context = {"colors" : color_schemes, 'form': form }            
        return render (request, 'sites/newbusiness.html', context);
    else:
        return redirect ("login")
   
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
        
from django.db.models import Avg
def reviews (request, business_id):
    business = Business.objects.get(pk=business_id)
    reviews = business.b_reviews.all()
    #calculate de medi of reviews score
    avg = reviews.aggregate(Avg('score')).get('score__avg')
    context = {"business": business,"reviews":reviews, "average" : avg }
    return render (request, "sites/reviews.html", context)

def new_review (request, business_id):
    if request.user.is_authenticated:
        business = Business.objects.get(pk=business_id)
        if request.method == 'POST':
            review_form = BusinessReview (person=request.user, review_for=business)   
            form = ReviewForm (request.POST, instance=review_form)      
            if form.is_valid():
                form.save()
                return redirect (reviews, business_id = business_id ) 
        else:
            # get method, prepare the form            
            form = ReviewForm ()
            context = {
            'business':business,
            'form':form
            }
        return render (request, "sites/new_review.html", context)            
    return redirect('login')
   
    
def colorscheme (request):
    schemes = ColorScheme.objects.all()
    return render(request,'sites/schemes.html', {'schemes':schemes})

#11/20/2021
def updatebiz (request, biz_id):
    color_schemes = ColorScheme.objects.all()
    biz = Business.objects.get (pk = biz_id )
    form = BusinessForm(instance=biz)
    
    if request.method=='POST':       
        form = BusinessForm(request.POST, request.FILES, instance=biz)
        if form.is_valid():
            form.save()
            return redirect("index")
        
    context = {"biz":biz, "form":form,"colors" : color_schemes}
    return render (request, 'sites/newbusiness.html', context);
    
 
 #12/14/2021
 #implementing search method
 # will iterate over each buisiness, and create a string with all fields
 # then will be used the method ifContain for each word in the find string 

def filter_biz (find):
    #get all the business
    business = Business.objects.all();
    #get all the word to match
    words = find.upper().split(" ");    
    result = []
    for biz in business:
        bizWords = biz.getWords().split(" ")
        check = any (item in bizWords for item in words)
        #result.append(bizWords)
        if check :
            result.append(biz)
    return result
    
def search( request ) :    
    if request.method=='POST':
        find = request.POST['find']
        biz = filter_biz(find)
        #Paginator
        paginator = Paginator(biz, 9)
        page_number = request.GET.get('page')
        business = paginator.get_page(page_number) 
        context = {"business": business }
        return render (request, 'sites/index.html', context )
   
def url_search (request, find):
        biz = filter_biz(find)
        #Paginator
        paginator = Paginator(biz, 9)
        page_number = request.GET.get('page')
        business = paginator.get_page(page_number) 
        context = {"business": business }
        return render (request, 'sites/index.html', context )


    
        
        
    