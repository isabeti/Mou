from django.urls import path
from . import views

urlpatterns = [
    path('create/post/', views.CreatePost.as_view(), name='create-post'),
    path('list/posts/', views.ListPosts.as_view(), name='list-posts'),
    path('detail/posts/<int:pk>/', views.DetailPost.as_view(), name='detail-posts'),
    path('action/posts/<int:pk>/', views.ActionPost.as_view(), name='action-posts'),
    path('list/of/liked/posts/', views.ListLikedPosts.as_view(), name='list-liked-posts'),
    path('list/of/view/posts/', views.ListViewPosts.as_view(), name='list-view-posts'),
    path('list/of/saved/posts/', views.ListSavedPosts.as_view(), name='list-liked-posts'),
]