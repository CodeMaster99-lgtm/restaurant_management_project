from django.http import JsonResponse
from django.shortcuts import render

def menu_page(request):
    return render(request, 'menu.html')

def  get_menu_items(request):

    menu_items = [
        {"id":1,"name":"Margherita Pizza", "price": 250},
        {"id":2, "name": "Veg Burger", "price": 120},
        {"id": 3,"name": "Pasta Alfredo", "price":200},
        {"id":4,"name":"Cold Coffee", "price":90},
    ]
    return JsonResponse(menu_items, safe=False)

