from appsecrets import AVATARS_TOTAL
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from . models import avatar_url
from appsecrets import *

avatars = []

class SignUpView (CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
  

def change_avatar (request):
    print("changing avatar")
    if not avatars:
        for id in range(0, AVATARS_TOTAL):
            avatar = { "id" : id,
                       "url" : avatar_url (id) }
            avatars.append (avatar)
    
    context ={"avatars":avatars}
    return render (request,"users/avatars.html", context)

def profile (request):
    return render (request,"users/profile.html")

def update_avatar (request, id):
    user = request.user
    user.avatar = id
    user.save();
    return redirect("index")