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
    # we don't need a context dictionary here
    return render(request, 'rango/about.html')


