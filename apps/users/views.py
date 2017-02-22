from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from .models import Person

def index(request):
    all_persons = Person.objects.all
    html = ''
    for person in all_persons:
        url = '/users/' + str(person.id) + '/'
        html += '<a href="'+ url + '#">'+ Person.first_name + '</a><br>'
    return HttpResponse(html)

def detail(request, person_id):
    return HttpResponse("<h2>details for user_id: " + str(person_id)+ "</h2>")
