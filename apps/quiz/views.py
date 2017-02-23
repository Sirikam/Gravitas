from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from .models import Quiz, Question, Answer


def index(request):
    template = loader.get_template("../templates/quiz/main.html")
    return HttpResponse(template.render())

def create(request):
    template = loader.get_template("../templates/quiz/professor.html")
    return HttpResponse(template.render())

def use(request):
    template = loader.get_template("../templates/quiz/student.html")
    return HttpResponse(template.render())

def admin(request):
    return render(request, "../templates/courses/admin.html",
                  {'Quiz': Quiz.objects.all(),
                   'Question': Question.objects.all(),
                   'Answer': Answer.objects.all()}
                  )