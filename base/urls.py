from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('add',add,name='add'),
    path('complete/<int:id>/',complete,name='complete'),
    path('trash',trash_list,name= 'trash'),
    path('trash/<int:id>/',trash_task,name='trash_task'),
    path('about',about,name='about'),
    path('completed',complete_list,name='completed'),
    path('edit/<int:id>/',edit, name='edit'),
    path('delete/<int:id>/',delete,name='delete'),
    path('restore/<int:id>/',restore,name='restore'),
]