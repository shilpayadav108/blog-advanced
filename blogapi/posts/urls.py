from django.contrib import admin
from django.urls import path,include
from rest_framework import authentication
# 
from . import views
from .views import PostList, PostDetail

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    
]
