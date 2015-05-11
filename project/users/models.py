from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    email = models.CharField(max_length=128, unique=True)
    first_name = models.CharField(max_length=128, null=True, blank=True, default=None)
    last_name = models.CharField(max_length=128, null=True, blank=True, default=None)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
