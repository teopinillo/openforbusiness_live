from django.urls import path
#from .views import SignUpView, show_avatars, change_avatar, set_avatars
#from django.contrib.auth import views as auth_views

from .views import listed, index, newbusiness 
from .views import updatebiz, audit, setfavorite 
from .views import myfavorites, reviews, new_review, colorscheme, search, url_search

#sites urls

urlpatterns = [    
    path ('my_business', listed, name = 'listed'),
    path ('newbusiness', newbusiness, name = 'newbusiness'),
    path ('updatebusiness/<int:biz_id>', updatebiz, name = 'updatebiz'),
    path ('', index, name = 'index'),
    path ('index', index, name = 'index'),    
    path ('audit', audit, name='audit' ),
    path ('setfavorite/<str:state>/<int:business_id>', setfavorite, name='setfavorite'),    
    path ('myfavorites', myfavorites, name='myfavorites' ),    
    path ('review/<int:business_id>', reviews, name='reviews' ),
    path ('new_review/<int:business_id>', new_review, name='new_review' ),
    path ('colorscheme', colorscheme, name='colorscheme'),
    path ('search', search, name='search'),
    path ('<str:find>', url_search, name='url_search'),
    
    
]
