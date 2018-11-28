from django.db import models
from django.urls import reverse_lazy
# Create your models here.


class BlogPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("blog_app:blog_detail", args=[str(self.pk)])