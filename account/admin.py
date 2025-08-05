from django.contrib import admin
from .models.user import UserProfile
from .models.menu import menu
from .models.order import Order

admin.site.register(UserProfile)
admin.site.register(Menu)
admin.site.register(Order)
