from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    user = models.CharField(max_length=30, blank=True)
    apellido = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)