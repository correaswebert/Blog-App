from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    TagPostListView,
    PostCommentView,
)
from . import views

# redirects from our app to our views
urlpatterns = [
    # empty path indicates that this is the index/home page
    path('', PostListView.as_view(), name="blog-home"),

    path('user/<str:username>/', UserPostListView.as_view(), name="user-posts"),
    path('tag/<str:name>/', TagPostListView.as_view(), name="tag-posts"),

    # use the default url instead of renaming it the views.py
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),

    # this view shares a template, so the template's default name is different
    path('post/new/', PostCreateView.as_view(), name="post-create"),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),

    path('post/<int:pk>/comment/', PostCommentView.as_view(), name="post-comment"),
]
