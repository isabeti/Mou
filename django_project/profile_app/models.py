from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile/image/')

    followers = models.ManyToManyField(User, blank=True, related_name='user_followers')
    firends = models.ManyToManyField(User, blank=True, related_name='user_firends')

    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)