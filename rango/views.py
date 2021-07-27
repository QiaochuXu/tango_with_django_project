from django.shortcuts import render
from django.http import HttpResponse

# create a index view
def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")

# create a about view
def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")


