from django.db.models import query_utils
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import EventForm
from .models import tt, participants
from django.contrib import messages
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
            y = str(uuid.uuid4())
            event_name = form.cleaned_data['event_name']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            place = form.cleaned_data['place']
            address = form.cleaned_data['address']
            print(date, time, place, address)
            trial = tt(date=str(date), time=time, host=request.user.username, place=place, info=address, unique_id=y, event_name=event_name)
            trial.save()
            return redirect("/schedule/")
    return HttpResponse('not thank you')

def display_info(request):
    if (request.method=='GET'):
        # getting all the objects of Map
        tt_1 = tt.objects.all()
        return render(request, 'display_page.html', {'tt_1': tt_1})
    if (request.method=='POST'):
        # getting all the objects of Map
        tt_1 = tt.objects.all()
        return render(request, 'display_page.html', {'tt_1': tt_1})

def send_data(request):
    if (request.method=='POST'):
        unique_id = request.POST['hidden_unique_id']
        event_name = request.POST['hidden_event_name']
        date = request.POST['hidden_date']
        time = request.POST['hidden_time']
        place = request.POST['hidden_place']
        try:
            mydb = MySQLdb.connect(
                "localhost",
                "root",
                "",
                "plantation"
            )
        except:
            print("Can't connect to database")
            return
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM schedule_participants")
        result = mycursor.fetchall()
        flag = 0
        for i in result:
            if unique_id in i:
                print('already there')
                flag = 1
                break
            else:
                print('not there')
        if flag == 0:
            trial = participants(name=request.user.username, email=request.user.email, unique_id=unique_id, event_name=event_name, date=date, time=time, place=place)
            trial.save()
        elif flag==1:
            # return redirect("/schedule/", flag='1')
            tt_1 = tt.objects.all()
            return render(request, 'display_page.html', {'flag': 1, 'tt_1': tt_1})
        return redirect("/schedule/")
    return redirect("/schedule/")

def delete_data(request):
    if (request.method=='POST'):
        unique_id = request.POST['hidden_unique_id']
        try:
            mydb = MySQLdb.connect(
                "localhost",
                "root",
                "",
                "plantation"
            )
        except:
            print("Can't connect to database")
            return
        mycursor = mydb.cursor()
        query = "DELETE FROM schedule_tt WHERE unique_id='"+unique_id+"'"
        mycursor.execute(query)
        mydb.commit()
        query_2 = "DELETE FROM schedule_participants WHERE unique_id='"+unique_id+"'"
        mycursor.execute(query_2)
        mydb.commit()
        return redirect("/schedule/")

