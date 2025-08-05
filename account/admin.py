from django.contrib import admin
from .models.user import UserProfile

admin.site.register(UserProfile)
