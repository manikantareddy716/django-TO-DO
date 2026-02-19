from django.urls import path
from .views import *

urlpatterns = [
    path('profile',profile,name='profile'),
    path('register',register,name='register'),
    path('login_',login_,name='login_'),
    path('logout/', logout_, name='logout'),
    
]
