from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class person(AbstractUser):
    first_name = models.CharField(50)
    middle_name = models.CharField(50)
    last_name = models.CharField(50)
    email = models.CharField(150)
    professor = bool()
