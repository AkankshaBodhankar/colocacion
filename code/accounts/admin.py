from django.contrib import admin
from .models import UserDetails, UserProfile

admin.site.register(UserDetails)
admin.site.register(UserProfile)