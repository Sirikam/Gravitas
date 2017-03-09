from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


def index(request):
    template = loader.get_template("../templates/documents/main.html")
    return HttpResponse(template.render())


def tdt4180(request):
    template = loader.get_template("documents/tdt4180.html")
    return HttpResponse(template.render())


def tdt4120(request):
    template = loader.get_template("documents/tdt4120.html")
    return HttpResponse(template.render())


def tdt4145(request):
    template = loader.get_template("documents/tdt4145.html")
    return HttpResponse(template.render())
