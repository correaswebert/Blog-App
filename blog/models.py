from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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

    def __str__(self):
        return self.title
