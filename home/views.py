# Code adapted from the CI Boutique Ado mini project

from django.shortcuts import render

# Create views here

def index(request):
    """ A view to return index page """
    return render(request, 'home/index.html')