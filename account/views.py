from django.shortcuts import render
from .models import menuItem

def menu_view(request):
    menu = MenuItem.objects.all()
    return render(request, 'home/menu.html',{'menu':menu})