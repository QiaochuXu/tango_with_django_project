from django.shortcuts import render
from django.http import HttpResponse

# create a index view
def index(request):
    # update the index() view
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # return a complete HTML page
    return render(request, 'rango/index.html', context = context_dict)

# create a about view
def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")


