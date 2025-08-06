from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

def menu_page(request):
    phone_number = settings.RESTAURANT_PHONE
    return render(request, 'home/menu.html',{'phone':phone_number})

def  get_menu_items(request):

    menu_items = [
        {"id":1,"name":"Margherita Pizza", "price": 250},
        {"id":2, "name": "Veg Burger", "price": 120},
        {"id": 3,"name": "Pasta Alfredo", "price":200},
        {"id":4,"name":"Cold Coffee", "price":90},
    ]
    return JsonResponse(menu_items, safe=False)



