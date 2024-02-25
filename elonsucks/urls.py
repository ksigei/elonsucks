from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_transaction/', views.create_transaction, name='create_transaction'),
    path('mine_block/', views.mine_block, name='mine_block'),
    path('chain/', views.chain, name='chain'),
]
