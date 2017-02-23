from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from .models import Course
# Create your views here.

def index(request):

    return render(request, "../templates/courses/admin.html",
                  {'Course': Course.objects.all()}
                  )
