from django.db import models
from django.contrib.auth.models import User
from categories.models import Category




class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    creat_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    is_show = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    picture = models.ImageField(upload_to='article')
    categories = models.ManyToManyField(Category , blank=True)

