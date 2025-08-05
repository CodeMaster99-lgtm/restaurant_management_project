from django.urls import path
from .views import *

urlpatterns = [

    path('', views.menu_view, name='menu'),
    
]