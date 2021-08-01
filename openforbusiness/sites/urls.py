from django.urls import path
#from .views import SignUpView, show_avatars, change_avatar, set_avatars
#from django.contrib.auth import views as auth_views

from .views import plan_a, icons

#sites urls

urlpatterns = [
    path('plan_a', plan_a, name = 'plan_a'),  
    path('icons', icons, name = 'icons'), 
]
