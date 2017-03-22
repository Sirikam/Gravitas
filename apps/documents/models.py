from django.db import models

from apps.courses.models import Course
from django.contrib.auth.models import User
# Create your models here.

class Document(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    name =  models.CharField(max_length=150, default='')
    private = models.BooleanField(1, default=1)

