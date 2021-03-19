from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from .models import Blog
import MySQLdb
import uuid
from .past_or_present import past_or_present
import threading
# Create your views here.

def index(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'index.html')

def get_name(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            y = str(uuid.uuid4())
            address = form.cleaned_data['address']
            maps_link = form.cleaned_data['maps_link']
            area = form.cleaned_data['area']
            permission_required = form.cleaned_data['permission_required']
            contact_management_name = form.cleaned_data['contact_management_name']
            contact_management_num = form.cleaned_data['contact_management_num']
            trial = Blog(user=request.user.username, address=address, maps_link=maps_link, area=area, permission_required=str(permission_required),contact_management_name=contact_management_name, contact_management_num=contact_management_num, unique_id=y)
            trial.save()
            # print('hello')
            return redirect('/maps/bloginfo')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'name.html', {'form': form})

def delete_blog(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
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
        query = "DELETE FROM maps_blog WHERE unique_id='"+unique_id+"'"
        mycursor.execute(query)
        mydb.commit()
        return redirect('/maps/bloginfo')

def display_blog_info(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    if (request.method=='GET'):
        # getting all the objects of Map
        Blogs = Blog.objects.all()
        return render(request, 'maps_blog.html', {'blog_data': Blogs})
    return redirect('/geofence/display_maps/')