from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

import random
# from Tag_Generator import generate_tags


def generate_tags(x):
    tags = random.sample(
        ['business', 'sports', 'politics', 'entertainment'],
        k=random.randint(1, 4))
    return ','.join(tags)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    likes = models.IntegerField(default=0)

    # for auto-recommendation system ()
    # topic = models.SmallIntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """override parent class' method, done to save tags"""
<<<<<<< HEAD
        super(Post,self).save(*args,**kwargs)
        current_tags = [tag for tag in Tag.objects.all()]
        for i in generate_tags(self.content).split(','):
            if i not in current_tags:
                tags = Tag(name=i)
                tags.save()
            else:
                tags = current_tags.filter(name=i)
            self.tags.add(tags)
=======
        super().save(*args, **kwargs)

        curr_tags = [tag.name for tag in Tag.objects.all()]
        post_tags = generate_tags(self.content).split(',')
>>>>>>> b2e3509e16e7897d635d129d22db988326dd70ac

        for t in post_tags[:4]:
            t = t.strip()

            if t in curr_tags:
                tag = Tag.objects.filter(name=t).first()
            else:
                tag = Tag(name=t)
                tag.save()

            self.tags.add(tag)

    def get_absolute_url(self):
        """route to url returned as a string from reverse"""
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    # one post can have many comments
    # ForeignKey is ManyToManyField
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post.title
