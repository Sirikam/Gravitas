from django.db import models

from django.contrib.auth.models import User


class Course(models.Model):
    course_code = models.CharField(max_length=25)
    course_name = models.CharField(max_length=50)
    lecturer = models.ManyToManyField(User, default='')

    def __str__(self):
        return self.course_code
