from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

# create a index view
def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in our context_dict dictionary (with our boldmessage!)
    # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    # update the index() view
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    context_dict['categories'] = category_list
    
    # render the response and send it back
    return render(request, 'rango/index.html', context = context_dict)

# create a about view
def about(request):
    # we don't need a context dictionary here
    return render(request, 'rango/about.html')


