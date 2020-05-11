from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Post(models.Model):
    # title can have maximum 100 characters
    title = models.CharField(max_length=100)

    # similar to CharField, but for longer texts
    content = models.TextField()

    # give option to set the date or use the current date as default
    date_posted = models.DateTimeField(default=timezone.now)

    # create one-to-many relationship using ForeignKey
    # one user can have multiple posts
    # delete all posts created by user when user is deleted - CASCADE
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # every post will be tagged using our NLP model
    tags = models.ManyToManyField(Tag)

    # number of likes a post gets from all users
    likes = models.IntegerField(default=0)

    # comment = models.TextField()

    def __str__(self):
        return self.title

    # instead or redirecting, we want the view to handle the routing
    # so we use the reverse function.
    def get_absolute_url(self):
        """route to url returned as a string from reverse"""
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    # one post can have many comments
    # ForeignKey is ManyToManyField
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title
