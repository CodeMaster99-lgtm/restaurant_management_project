from django.urls import path
from .views import *

urlpatterns = [
    path('menu/', views.menu_list, name='menu_list'),
    path('order/',views.order_create, name='order_create'),
]