from django.urls import path
#from .views import SignUpView, show_avatars, change_avatar, set_avatars
#from django.contrib.auth import views as auth_views

from .views import listed, index, newbusiness, audit, setfavorite, myfavorites, reviews, new_review, test, colorscheme

#sites urls

urlpatterns = [    
    path('my_business', listed, name = 'listed'),
    path('newbusiness', newbusiness, name = 'newbusiness'),
    path('', index, name = 'index'),
    path('index', index, name = 'index'),    
    path('audit', audit, name='audit' ),
    path('setfavorite/<str:state>/<int:business_id>', setfavorite, name='setfavorite'),    
    path('myfavorites', myfavorites, name='myfavorites' ),
    path('new_review/<int:business_id>', new_review, name='new_review' ),
    path('review/<int:business_id>', reviews, name='reviews' ),
    path('test/<int:business_id>', test, name='test' ),
    path('colorscheme', colorscheme, name='colorscheme'),
    
]
