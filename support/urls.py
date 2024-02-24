from django.urls import path
from . import views

urlpatterns = [
    # path('', views.support_ticket_list, name='support_ticket_list'),
    path('<uuid:pk>/', views.support_ticket_detail, name='support_ticket_detail'),
    path('create/', views.create_support_ticket, name='create_support_ticket'),
    path('<uuid:pk>/update/', views.update_support_ticket, name='update_support_ticket'),
    path('<uuid:pk>/delete/', views.delete_support_ticket, name='delete_support_ticket'),
]
