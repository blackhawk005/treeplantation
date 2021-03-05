from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from schedule.models import tt, participants, pastevents
from maps.models import Blog
import MySQLdb
from .past_or_present import past_or_present

# Create your views here.

# home page
def index(request):
    past_or_present()
    past_presents = pastevents.objects.all()
    return render(request, 'home/index.html', {'past_presents':past_presents})

# login page
def login_page(request):
    past_or_present()
    if (request.method == 'POST'):
        user_name = request.POST['user_name']
        pass_word = request.POST['pass']
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("Login Failed")
    else:
        return render(request, 'home/login.html')

# registration page
def register(request):
    past_or_present()
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if (pass1 == pass2):
            if (User.objects.filter(username=user_name).exists()):
                return HttpResponse("Username Taken")
            elif (User.objects.filter(email=email).exists()):
                return HttpResponse("Email already used")
            else:
                user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name, email=email, password=pass1)
                user.save()
                return redirect('/login/')
        else:
            return HttpResponse("Passwords do not match")
    else:
        return render(request, 'home/register.html')

def profile(request):
    past_or_present()
    tt_1 = tt.objects.all()
    participants_1 = participants.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'home/profile.html', {'tt_1': tt_1, 'participants_1': participants_1, 'blogs': blogs})

def delete_hosted_event(request):
    past_or_present()
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
    return redirect('/profile')

def delete_participated_events(request):
    past_or_present()
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
    query = "DELETE FROM schedule_participants WHERE unique_id='"+unique_id+"'"
    mycursor.execute(query)
    mydb.commit()
    return redirect('/profile')

def delete_map_blog(request):
    past_or_present()
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
    query = "DELETE FROM maps_blog WHERE unique_id='"+unique_id+"'"
    mycursor.execute(query)
    mydb.commit()
    return redirect('/profile')

# logout page
def logout_page(request):
    past_or_present()
    logout(request)
    return redirect('/')

# how it works page
def functionality(request):
    past_or_present()
    return render(request, 'home/functionality.html')

# about page
def about(request):
    past_or_present()
    return render(request, 'home/about.html')

# contact us page
def contact_us(request):
    past_or_present()
    return render(request, 'home/contact_us.html')

