from django.db import models
from django.contrib.auth.models import User
from apps.courses.models import Course

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    PROFESSOR = 'PR'
    COORDINATOR = 'CO'
    STUDENT = 'ST'
    PERSON_ROLE = (
        (PROFESSOR, 'Professor'),
        (COORDINATOR, 'Coordinator'),
        (STUDENT, 'Student'),
    )
    role_in_app = models.CharField(
        max_length=2,
        default=STUDENT,
    )


    def __str__(self):
        return  self.first_name + ' ' + self.last_name

