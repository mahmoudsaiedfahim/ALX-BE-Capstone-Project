from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Extending AbstractUser.
class CustomUser (AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=50, unique=True)
    

