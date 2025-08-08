from django.shortcuts import render
from .models import Menu, Order
from .forms import OrderForm
from .models import Restaurant

def homepage(request):
    restaurant =
Restaurant.objects.first()  #
Assuming you have at least one
entry
return render(request,'homepage.html',{'restaurant_name':})


def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'menu_list.html', {'menus':menus})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})
