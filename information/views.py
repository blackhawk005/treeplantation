from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'info/index.html')

def indoor(request):
    return render(request, 'info/indoor.html')

def page_open_lemon(request):
    return render(request, 'indoor_plants/lemon.html')

def page_open_curry(request):
    return render(request, 'indoor_plants/curry.html')