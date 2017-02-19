from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>A page for the quiz app</h1>")

#def create(request):
 #   return render(request, "quiz/proffesor.html")

#def use(request):
 #   return render(request, "quiz/student.html")

#def admin(request):
 #   return render(request, "quiz/admin.html")