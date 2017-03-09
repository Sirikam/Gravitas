from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.views.generic import TemplateView


def index(request):
    template = loader.get_template("../templates/staticpages/home.html")
    return HttpResponse(template.render())


class home(TemplateView):
    template = loader.get_template("../templates/staticpages/home.html")


def login(request):
    template = loader.get_template("../templates/staticpages/login.html")
    return HttpResponse(template.render())


def homepage(request):
    template = loader.get_template("../templates/staticpages/homepage.html")
    return HttpResponse(template.render())
