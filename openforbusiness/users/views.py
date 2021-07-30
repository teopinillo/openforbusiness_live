from appsecrets import AVATARS_TOTAL
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import Avatar, CustomUser
from appsecrets import *

avatars = []

class SignUpView (CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

# Return's the full url
def get_avatar_url (id):
        return AVATARS_URL + str(id).zfill(4) + ".jpeg"
    
def show_avatars(request):
    if not avatars:
        for id in range(0, AVATARS_TOTAL):
            avatar = { "id" : id,
                       "url" : get_avatar_url (id) }
            avatars.append (avatar)
    
    context ={"avatars":avatars}
    return render (request,"users/avatars.html", context)


def change_avatar(request, pk):
    user = request.user
    avatar = Avatar.objects.get (id=pk)
    user.avatar = avatar
    user.save()
    return redirect('index')

def set_avatars(request):    
    avatars = Avatar.objects.all()
    context ={"avatars":avatars}
    return render (request,"users/avatars.html", context)

def profile (request, pk):
    return render (request,"users/profile.html")

"""def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            avatar = Avatar()
            avatar.save()
            user = CustomUser.objects.create_user(
                username, email, password, avatar=avatar)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
        """