from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to='users/avatar')
    about_me = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}'