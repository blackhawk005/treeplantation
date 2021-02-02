from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.

# home page
def index(request):
    return render(request, 'home/index.html')

# login page
def login_page(request):
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

# logout page
def logout_page(request):
    logout(request)
    return redirect('/')

# how it works page
def functionality(request):
    return render(request, 'home/functionality.html')

# about page
def about(request):
    return render(request, 'home/about.html')

# contact us page
def contact_us(request):
    return render(request, 'home/contact_us.html')

