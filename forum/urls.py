from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_post_list, name='forum_post_list'),
    path('<uuid:pk>/', views.forum_post_detail, name='forum_post_detail'),
    path('create/', views.create_forum_post, name='create_forum_post'),
    path('<uuid:pk>/update/', views.update_forum_post, name='update_forum_post'),
    path('<uuid:pk>/delete/', views.delete_forum_post, name='delete_forum_post'),
]
