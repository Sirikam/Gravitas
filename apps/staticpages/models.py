from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=250)
    profession = models.CharField(max_length=150)
    profile_picture = models.CharField(max_length=1000)

class register(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)