from django.urls import path
from .views import SignUpView, show_avatars, change_avatar, set_avatars, profile
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup'),
    path('change_password/', auth_views.PasswordChangeView.as_view(), name="change-password"),
    path('avatars/', show_avatars, name="avatars"),
    path('avatars/init', set_avatars, name="set_avatars"),
    path('avatars/change/<int:pk>',change_avatar, name ="change_avatar"),
    path('profile/<int:pk>', profile, name='profile'),
]
