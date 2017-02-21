from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    template = loader.get_template("../templates/users/main.html")
    return HttpResponse(template.render())

def detail(request, person_id):
    return HttpResponse("<h2>details for user_id: " + str(person_id)+ "</h2>")
