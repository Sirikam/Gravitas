from django.db import models


class Course(models.Model):
    course_code = models.CharField(max_length=25)
    course_name = models.CharField(max_length=50)
    lecturer = models.CharField(max_length=150)

    def __str__(self):
        return self.course_code
