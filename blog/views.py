from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


def home(request):
    """home page traffic is handled here"""

    # dynamic data passed to the template
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post

    # default location is <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'

    # template uses posts context name (default is object_list)
    context_object_name = 'posts'

    # blogs are ordered from newest to oldest
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


# the mixin is like the login_required decorator
# you cannot create posts unless logged in
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """set the author of the post to current user before posting"""

        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """set the author of the post to current user before posting"""

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """only the author of the post can update it"""

        # get reference to the current post
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    # redirect to homepage on deleting post
    success_url = '/'

    def test_func(self):
        """only the author of the post can update it"""

        # get reference to the current post
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


def about(request):
    """about page traffic is handled here"""
    return render(request, 'blog/about.html', {'title': 'About'})
