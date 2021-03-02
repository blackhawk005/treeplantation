from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import GeeksForm
# from .models import Blog
import MySQLdb
import uuid

# Create your views here.
def index(request):
    context = {} 
    context['form'] = GeeksForm() 
    return render( request, "create_event.html", context)
