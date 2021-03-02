from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import EventForm
from .models import tt
import MySQLdb
import uuid

# Create your views here.
def index(request):
    if (request.method=='GET'):
        # getting all the objects of Map
        tt = tt.objects.all()
        return render(request, 'create_event.html', {'tt_index': tt})
    return render( request, "create_event.html")

def form_fill(request):
    return render( request, "create_event.html")

def info_send(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            print('if executed')
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            place = form.cleaned_data['place']
            address = form.cleaned_data['address']
            print(date, time, place, address)
            trial = tt(date=str(date), time=time, host=request.user.username, place=place, info=address)
            trial.save()
            return HttpResponse('thank you')
    return HttpResponse('not thank you')
