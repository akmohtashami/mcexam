from django.shortcuts import render
from exams import views

# Create your views here.

def index(request):
    return render(request, "base.html")