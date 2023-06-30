from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """A custom user for extension"""
    pass


    def __str__(self):
        return self.username
