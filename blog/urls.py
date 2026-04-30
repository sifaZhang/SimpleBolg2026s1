from django.contrib.auth import login, logout
from django.urls import path, include

from blog.views import index, category_detail, post_detail, create_category, PostListView, PostDetailView, \
    PostCreateView, PostUpdateView, PostDeleteView, register, create_users, like_unlikes, add_comments

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:post_id>', post_detail, name='post_detail'),
    path('category/<int:category_id>', category_detail, name='category_detail'),

    path('create_category', create_category, name='create_category'),

    # path('create_post', create_post, name='create_post'),
    path('posts/', PostListView.as_view(), name='post_list'),

    path('post_detail/<int:pk>/detail', PostDetailView.as_view(), name='post_detail_view'),

    path('post_create/', PostCreateView.as_view(), name='post_create'),

    path('post_update/<int:pk>', PostUpdateView.as_view(), name='post_update'),

    path('post_delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),

    path('register/', register, name='register'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('create_users/', create_users, name='create_users'),

    path('like_unlikes/<int:post_id>', like_unlikes, name='like_unlikes'),
    path('add_comments/<int:post_id>', add_comments, name='add_comments'),
]


