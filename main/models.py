from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    date = models.DateField(default=timezone.now)
    body = RichTextField(config_name='admin')
    img_url = models.CharField(max_length=250)
    views = models.IntegerField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    parent_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    text = models.TextField()

    def __str__(self):
        return self.parent_post.title


class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.email


class Visitor(models.Model):
    date_time = models.DateTimeField()
    ip = models.CharField(max_length=100)
    user_agent = models.CharField(max_length=300)
