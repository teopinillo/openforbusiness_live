from django.contrib import admin
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin (UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','avatar',] 
    list_editable = ('email','avatar',)

admin.site.register (CustomUser, CustomUserAdmin)


