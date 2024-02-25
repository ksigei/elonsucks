from django.contrib import admin

# Register your models here.
from .models import Wallet, Transaction, Block, Node

adm_list = [
    Wallet, Transaction, Block, Node
]

admin.site.register(adm_list)