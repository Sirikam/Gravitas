from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class person(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    professor = bool(1)

    def __str__(self):
        return  self.first_name + ' ' + self.last_name

