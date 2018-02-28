from django.urls import path
from .models import Post
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts_list'),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('new/', views.NewPostView.as_view(), name='post_new'),
    path('create/', views.create, name='post_create')
]