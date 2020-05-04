from django.contrib import admin
from .models import Post


# add the Post model to our admin page, along with Users and Groups
admin.site.register(Post)
