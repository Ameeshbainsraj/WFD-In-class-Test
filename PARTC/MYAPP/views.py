from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, SENJA, GO TO MODEL.PY TO SEE MY WORK!</h1>")
