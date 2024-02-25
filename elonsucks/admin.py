from django.contrib import admin

# Register your models here.
from .models import Wallet, Transaction, Block

adm_list = [
    Wallet, Transaction, Block
]

admin.site.register(adm_list)