from django.http import HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return render(request, 'simulator/index.html')
