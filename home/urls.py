from django.urls import path
from  .import views

urlpatterns = [

    path('menu/',views.menu_page, name='menu-page'),
    path('api/menu', views.get_menu_items, name='menu-api')
    
]