from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    return HttpResponse("<h1>A page for the quiz app</h1>")

def create(request):
    template = loader.get_template("../templates/quiz/proffesor.html")
    return HttpResponse(template.render())

def use(request):
    template = loader.get_template("../templates/quiz/student.html")
    return HttpResponse(template.render())

def admin(request):
    template = loader.get_template("../templates/quiz/admin.html")
    return HttpResponse(template.render())