from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Tag, Comment


class PostListView(ListView):
    model = Post

    # default location is <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'

    # template uses posts context name (default is object_list)
    context_object_name = 'posts'

    # blogs are ordered from newest to oldest
    ordering = ['-date_posted']

    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        """get all posts by user"""

        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class TagPostListView(ListView):
    model = Post
    template_name = 'blog/tag_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        """get all posts of a tag"""

        tag_name = get_object_or_404(Tag, name=self.kwargs.get('name'))
        return Post.objects.filter(tags=tag_name).order_by('-date_posted')


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


class PostCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        """set the author of the post to current user before posting"""

        post_id = self.request.path
        post_id = post_id.split('/')[2]
        self.success_url = f'/post/{post_id}'

        form.instance.author = self.request.user
        form.instance.post = Post.objects.filter(id=post_id).first()
        return super().form_valid(form)
