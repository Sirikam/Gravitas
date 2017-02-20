from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('staticpages/main.html')



