from django.urls import path
from . import views

urlpatterns = [
    path('create-category/', views.create_category, name='create_category'),
    
    path('create-post/', views.create_post, name='create_post'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('categories/', views.category_list, name='category_list'),
]
