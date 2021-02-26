from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from .models import Blog
import MySQLdb

# Create your views here.

def index(request):
    return render(request, 'index.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            maps_link = form.cleaned_data['maps_link']
            area = form.cleaned_data['area']
            permission_required = form.cleaned_data['permission_required']
            contact_management_name = form.cleaned_data['contact_management_name']
            contact_management_num = form.cleaned_data['contact_management_num']
            trial = Blog(user=request.user.username, address=address, maps_link=maps_link, area=area, permission_required=str(permission_required),contact_management_name=contact_management_name, contact_management_num=contact_management_num)
            trial.save()
            # print('hello')
            return redirect('/maps/bloginfo')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'name.html', {'form': form})

def display_blog_info(request):
	if (request.method=='GET'):
        # getting all the objects of Map
		Blogs = Blog.objects.all()
		return render(request, 'maps_blog.html', {'blog_data': Blogs})
	return redirect('/geofence/display_maps/')