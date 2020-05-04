from django.shortcuts import render


# dummy posts
posts = [
    {
        'author': 'Swebert Correa',
        'title': 'Blog Post 1',
        'content': 'First Post',
        'date_posted': 'May 3, 2020',
    },
    {
        'author': 'Jinit Sanghvi',
        'title': 'Blog Post 2',
        'content': 'Second Post',
        'date_posted': 'May 4, 2020',
    },
]


def home(request):
    """home page traffic is handled here"""

    # dynamic data passed to the template
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    """about page traffic is handled here"""
    return render(request, 'blog/about.html', {'title': 'About'})
