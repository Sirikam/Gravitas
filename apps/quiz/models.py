from django.db import models
from apps.courses.models import Course

# Create your models here.
class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default='')
    quiz_navn = models.CharField(max_length=50)
    maxQuestions = models.IntegerField(4, default=0)
    passedPercentage = models.CharField(max_length=50, default=0)

    def __str__(self):
        return self.quiz_navn

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    spoersmaal_stilt = models.CharField(max_length=1000)

    def __str__(self):
        return self.spoersmaal_stilt

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default='')
    answer_alt = models.CharField(max_length=100)
    isRight = models.BooleanField(1)

    def __str__(self):
        return self.answer_alt

