from django.shortcuts import render
from .models import Post


def home(request):
    """home page traffic is handled here"""

    # dynamic data passed to the template
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)


def about(request):
    """about page traffic is handled here"""
    return render(request, 'blog/about.html', {'title': 'About'})
