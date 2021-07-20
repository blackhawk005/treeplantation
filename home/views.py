from random import randint
from home.mysql import mysqldb
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from schedule.models import tt, participants, pastevents
from maps.models import Blog
from django.contrib import messages
import MySQLdb
from .past_or_present import past_or_present
import threading
from .models import users
from .send_mail import mail_seder
from home.user_check import user_check

# Create your views here.

# home page
def index(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    # past_or_present()
    past_presents = pastevents.objects.all()
    return render(request, 'home/index.html', {'past_presents':past_presents})

# login page
def login_page(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    if (request.method == 'POST'):
        user_name = request.POST['user_name']
        pass_word = request.POST['pass']
        if (User.objects.filter(username=user_name).exists()):
            pass
        else:
            messages.warning(request, 'Username Doesnot Exist')
            return redirect('/login/')
        user = authenticate(username=user_name, password=pass_word)
        # print('User Authentication: ',user)
        if user is not None:
            login(request, user)
            return redirect('/')
        elif user is None:
            messages.warning(request, 'Wrong Password')
            return redirect('/login/')
        else:
            messages.warning(request, 'Wrong Password')
            return redirect('/login/')
    else:
        return render(request, 'home/login.html')

# registration page
def register(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        if first_name == '':
            messages.warning(request, 'Please put your first name')
            return redirect('register')
        else:
            pass
        last_name = request.POST['last_name']
        if last_name == '':
            messages.warning(request, 'Please put your last name')
            return redirect('register')
        else:
            pass
        user_name = request.POST['username']
        if user_name == '':
            messages.warning(request, 'Please put a username')
            return redirect('register')
        else:
            pass
        email = request.POST['email']
        if email == '':
            messages.warning(request, 'Please put an email')
            return redirect('register')
        else:
            pass
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if (pass1 == pass2):
            if (User.objects.filter(username=user_name).exists()):
                messages.warning(request, 'Username Already Taken')
                return redirect('register')
            elif (User.objects.filter(email=email).exists()):
                messages.warning(request, 'Email Already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name, email=email, password=pass1)
                user.save()
                user_save = users(user=user_name, report='0')
                user_save.save()
            # mail_seder(receiver_email=email, user=result[0][0], event='', date='', place='', flag=3)
                t2 = threading.Thread(target=mail_seder, args=(email, user_name, '', '', '', 5))
                t2.start()
                return redirect('/login/')
        else:
            messages.warning(request, 'Password donot match')
            return redirect('register')
    else:
        return render(request, 'home/register.html')

def profile(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    tt_1 = tt.objects.all()
    participants_1 = participants.objects.all()
    blogs = Blog.objects.all()
    event_names = list(tt.objects.filter(host=request.user.username).values_list('unique_id', 'event_name'))
    print(event_names)
    x = []
    for i in range(len(event_names)):
        all_participants = list(participants.objects.filter(unique_id=event_names[i][0]).values_list('name'))
        y_1 = list(event_names[i])
        y_1.append(list(x[0] for x in all_participants))
        print(tuple(y_1))
        if len(all_participants) != 0:
            x.append(tuple(y_1))
    print(x)
    # print(all_participant)
    return render(request, 'home/profile.html', {'tt_1': tt_1, 'participants_1': participants_1, 'blogs': blogs, 'participants': x,})

def delete_hosted_event(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    unique_id = request.POST['hidden_unique_id']
    mydb = mysqldb()
    mycursor = mydb.cursor()
    query = "DELETE FROM schedule_tt WHERE unique_id='"+unique_id+"'"
    mycursor.execute(query)
    mydb.commit()
    query_2 = "DELETE FROM schedule_participants WHERE unique_id='"+unique_id+"'"
    mycursor.execute(query_2)
    mydb.commit()
    return redirect('/profile')

def delete_participated_events(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    unique_id = request.POST['hidden_unique_id']
    mydb = mysqldb()
    mycursor = mydb.cursor()
    query = "DELETE FROM schedule_participants WHERE unique_id='"+unique_id+"'"
    mycursor.execute(query)
    mydb.commit()
    return redirect('/profile')

def delete_map_blog(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    unique_id = request.POST['hidden_unique_id']
    mydb = mysqldb()
    mycursor = mydb.cursor()
    query = "DELETE FROM maps_blog WHERE unique_id='"+unique_id+"'"
    mycursor.execute(query)
    mydb.commit()
    return redirect('/profile')

# logout page
def logout_page(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    logout(request)
    return redirect('/')

# how it works page
def functionality(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    return render(request, 'home/functionality.html')

# about page
def about(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    return render(request, 'home/about.html')

# contact us page
def contact_us(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    t2 = threading.Thread(target=user_check)
    t2.start()
    return render(request, 'home/contact_us.html')

