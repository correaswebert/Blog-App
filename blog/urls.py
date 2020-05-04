from django.urls import path
from . import views

# redirects from our app to our views
urlpatterns = [
    # empty path indicates that this is the index/home page
    path('', views.home, name="blog-home"),

    path('about/', views.about, name="blog-about"),
]
