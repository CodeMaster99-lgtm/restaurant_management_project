from django.shortcuts import render, redirect
from .models import menuItem
from .models.order import order
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def menu_view(request):
    menu = MenuItem.objects.all()
    return render(request, 'home/menu.html',{'menu':menu})

@login_required
def place_order(request):
    if request.method == 'POST':
        item_ids = request.POST.getlist('items')
        total = 0
        items = []

        for item_id in item_ids:
            item = Menu.objects.get(id=item_id)
            items.append(item)
            total += item.price
        
        order = Order.objects.create(
            customer=request.user,
            total_amount=total,
            status='pending'
        )
        order.items.set(items)
        order.save()
        return redirect('menu')
    
    return redirect('menu')