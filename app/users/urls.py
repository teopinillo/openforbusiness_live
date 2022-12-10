from django.urls import path
from .views import change_avatar, SignUpView, profile, update_avatar
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('change_avatar', change_avatar, name="change_avatar"),
    path('update_avatar/<int:id>', update_avatar, name="update_avatar"),
    path('signup/', SignUpView.as_view(), name = 'signup'),
    path('change_password/', auth_views.PasswordChangeView.as_view(), name="change-password"),   
    path('profile/<int:pk>', profile, name='profile'),
]
