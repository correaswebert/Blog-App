from django.contrib import admin
from .models import Post, Comment


# add models to our admin page
admin.site.register(Post)
admin.site.register(Comment)
