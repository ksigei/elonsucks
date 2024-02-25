# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('mine-block/', views.mine_block, name='mine_block'),
    path('transfer/', views.transfer, name='transfer'),
]
