from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import EventForm
from .models import tt
import MySQLdb
import uuid

# Create your views here.

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
            return ( request, "display_page.html")
    return HttpResponse('not thank you')

def display_info(request):
    tt_1 = tt.objects.all()
    # print(tt_1[1])
    return render(request, 'display_page.html', {'tt_1': tt_1})

