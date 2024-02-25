from django.contrib import admin

# Register your models here.
from .models import UserProfile

adm_list = [
    UserProfile
]

admin.site.register(adm_list)