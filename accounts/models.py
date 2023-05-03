from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Account(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=255, blank=True)
    bio = models.TextField(max_length=225, blank=True)
    socials = models.ManyToManyField('Socials', related_name="medias", blank=True)
    profile_picture = models.ImageField(upload_to='userprofile', blank=True)

    def __str__(self):
        return self.email
class Socials(models.Model):
    link_name = models.CharField(max_length=255)
    link_url = models.URLField()