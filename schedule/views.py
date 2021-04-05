from django.db.models import query_utils
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import EventForm
from .models import tt, participants
from django.contrib import messages
import MySQLdb
import uuid
from .send_mail import send_email
from .past_or_present import past_or_present
import threading
import random
from .send_mail import mail_seder
from home.mysql import mysqldb
from home.user_check import user_check
from datetime import date, datetime

# Create your views here.

def form_fill(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    today = date.today()
    now = datetime.now()
    print("now =", now)

    rest_date_time = '2021-04-30 12:00:00'
    then = datetime.strptime(rest_date_time, '%Y-%m-%d %H:%M:%S')
    print("then=", then)
    if now < then:
        return render(request, "covid.html")
    return render( request, "create_event.html")

def create_event(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    today = date.today()
    now = datetime.now()
    print("now =", now)

    rest_date_time = '2021-04-30 12:00:00'
    then = datetime.strptime(rest_date_time, '%Y-%m-%d %H:%M:%S')
    print("then=", then)
    if now < then:
        return render(request, "covid.html")
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
            x = random.randint(1, 25)
            y_new = "/media/"+str(x)+".svg"
            trial = tt(date=str(date), time=time, host=request.user.username, place=place, info=address, unique_id=y, event_name=event_name,image=y_new, reported='0')
            trial.save()
            t1 = threading.Thread(target=send_email, args=(request.user.username, event_name, str(date), place, 1))
            t1.start()
            # send_email(username=request.user.username, event=event_name, date=str(date), place=place,flag=1)
            return redirect("/schedule/")
    return HttpResponse('not thank you')

def display_info(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    today = date.today()
    now = datetime.now()
    print("now =", now)

    rest_date_time = '2021-04-30 12:00:00'
    then = datetime.strptime(rest_date_time, '%Y-%m-%d %H:%M:%S')
    print("then=", then)
    if now < then:
        return render(request, "covid.html")
    if (request.method=='GET'):
        # getting all the objects of Map
        tt_1 = tt.objects.all()
        return render(request, 'display_page.html', {'tt_1': tt_1})
    if (request.method=='POST'):
        # getting all the objects of Map
        tt_1 = tt.objects.all()
        return render(request, 'display_page.html', {'tt_1': tt_1})

def send_data(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    today = date.today()
    now = datetime.now()
    print("now =", now)

    rest_date_time = '2021-04-30 12:00:00'
    then = datetime.strptime(rest_date_time, '%Y-%m-%d %H:%M:%S')
    print("then=", then)
    if now < then:
        return render(request, "covid.html")
    if (request.method=='POST'):
        unique_id = request.POST['hidden_unique_id']
        event_name = request.POST['hidden_event_name']
        date = request.POST['hidden_date']
        time = request.POST['hidden_time']
        place = request.POST['hidden_place']
        current_user = request.user.username
        print(current_user)
        # try:
        #     mydb = MySQLdb.connect(
        #         "localhost",
        #         "root",
        #         "",
        #         "plantation"
        #     )
        # except:
        #     print("Can't connect to database")
        #     return
        mydb = mysqldb()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM schedule_participants")
        result = mycursor.fetchall()
        flag = 0
        for i in result:
            if unique_id in i  and current_user in i:
                print('already there')
                flag = 1
                break
            else:
                print('not there')
        if flag == 0:
            send_email(username=request.user.username, event=event_name, date=date, place=place, flag=flag)
            trial = participants(name=request.user.username, email=request.user.email, unique_id=unique_id, event_name=event_name, date=date, time=time, place=place)
            trial.save()
        elif flag==1:
            # return redirect("/schedule/", flag='1')
            tt_1 = tt.objects.all()
            return render(request, 'display_page.html', {'flag': flag, 'tt_1': tt_1})
        return redirect("/schedule/")
    return redirect("/schedule/")

def delete_data(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    if (request.method=='POST'):
        unique_id = request.POST['hidden_unique_id']
        # try:
        #     mydb = MySQLdb.connect(
        #         "localhost",
        #         "root",
        #         "",
        #         "plantation"
        #     )
        # except:
        #     print("Can't connect to database")
        #     return
        mydb = mysqldb()
        mycursor = mydb.cursor()
        query = "DELETE FROM schedule_tt WHERE unique_id='"+unique_id+"'"
        mycursor.execute(query)
        mydb.commit()
        query_2 = "DELETE FROM schedule_participants WHERE unique_id='"+unique_id+"'"
        mycursor.execute(query_2)
        mydb.commit()
        return redirect("/schedule/")

def report_event(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    if (request.method=='POST'):
        unique_id = request.POST['hidden_unique_id']
        event_name = request.POST['hidden_event_name']
        print('unique_id:', unique_id)
        # try:
        #     mydb = MySQLdb.connect(
        #         "localhost",
        #         "root",
        #         "",
        #         "plantation"
        #     )
        # except:
        #     print("Can't connect to database")
        #     return
        mydb = mysqldb()
        flag = 3
        mycursor = mydb.cursor()
        query = "select * from home_users where user in (select user from schedule_tt where unique_id="+'"'+unique_id+'")'
        mycursor.execute(query)
        result = mycursor.fetchall()

        reports = result[0][1]

        identifying_id = unique_id.split('-')
        reporting_id = identifying_id[4]

        query = "select reported_event from home_users where user='"+str(request.user.username)+"'"
        mycursor.execute(query)
        check = mycursor.fetchall()

        print(check[0][0])
        checker = check[0][0].split()

        if reporting_id in checker:
            flag = 1
        else:
            query = "select email from auth_user where username ='" + result[0][0] + "'"
            mycursor.execute(query)
            email_list = mycursor.fetchall()
            email = email_list[0][0]
            # mail_seder(receiver_email=email, user=result[0][0], event='', date='', place='', flag=3)
            t2 = threading.Thread(target=mail_seder, args=(email, result[0][0], event_name, '', '', 4))
            t2.start()
            query = "select reported from schedule_tt where unique_id="+'"'+unique_id+'"'
            mycursor.execute(query)
            report_of_event = mycursor.fetchall()
            final_report_event = report_of_event[0][0]
            new_report_event = str(int(final_report_event) + 1)
            query = "update schedule_tt set reported='" + new_report_event + "' where unique_id='" + unique_id + "'"
            mycursor.execute(query)
            mydb.commit()
            if check[0][0] == '':
                new_reports = str(int(reports) + 1)
                query = "update home_users set report='" + new_reports + "' where user='" + result[0][0] + "'"
                mycursor.execute(query)
                mydb.commit()
                query = "update home_users set reported_event='"+reporting_id+"' where user='"+str(request.user.username)+"'"
                mycursor.execute(query)
                mydb.commit()
            else:
                new_reports = str(int(reports) + 1)
                query = "update home_users set report='" + new_reports + "' where user='" + result[0][0] + "'"
                mycursor.execute(query)
                mydb.commit()
                new_reporting_id = check[0][0] + ' ' + reporting_id
                query = "update home_users set reported_event='" + new_reporting_id + "' where user='"+str(request.user.username)+"'"
                mycursor.execute(query)
                mydb.commit()
        tt_1 = tt.objects.all()
        return render(request, 'display_page.html', {'flag_1': flag, 'tt_1': tt_1})


def terms(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    return render( request, "terms.html")


