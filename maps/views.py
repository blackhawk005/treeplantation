from schedule.send_mail import mail_seder, send_email
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from .models import Blog
import MySQLdb
import uuid
from .past_or_present import past_or_present
import threading
import random
from .send_mail import mail_seder
from home.mysql import mysqldb
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
            x = random.randint(1, 25)
            y_new = "/media/"+str(x)+".svg"
            trial = Blog(user=request.user.username, address=address, maps_link=maps_link, area=area, permission_required=str(permission_required),contact_management_name=contact_management_name, contact_management_num=contact_management_num, unique_id=y, image=y_new)
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
        mydb = mysqldb()
        mycursor = mydb.cursor()
        query = "DELETE FROM maps_blog WHERE unique_id='"+unique_id+"'"
        mycursor.execute(query)
        mydb.commit()
        return redirect('/maps/bloginfo')

def report_blog(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    if (request.method=='POST'):
        unique_id = request.POST['hidden_unique_id']
        print('unique_id:', unique_id)
        mydb = mysqldb()
        flag = 3
        mycursor = mydb.cursor()
        query = "select * from home_users where user in (select user from maps_blog where unique_id="+'"'+unique_id+'")'
        mycursor.execute(query)
        result = mycursor.fetchall()

        reports = result[0][1]
        identifying_id = unique_id.split('-')
        reporting_id = identifying_id[4]

        query = "select reported_map from home_users where user='"+str(request.user.username)+"'"
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
            t2 = threading.Thread(target=mail_seder, args=(email, result[0][0], '', '', '', 3))
            t2.start()
            if check[0][0] == '':
                new_reports = str(int(reports) + 1)
                query = "update home_users set report='" + new_reports + "' where user='" + result[0][0] + "'"
                mycursor.execute(query)
                mydb.commit()
                query = "update home_users set reported_map='"+reporting_id+"' where user='"+str(request.user.username)+"'"
                mycursor.execute(query)
                mydb.commit()
            else:
                new_reports = str(int(reports) + 1)
                query = "update home_users set report='" + new_reports + "' where user='" + result[0][0] + "'"
                mycursor.execute(query)
                mydb.commit()
                new_reporting_id = check[0][0] + ' ' + reporting_id
                query = "update home_users set reported_map='" + new_reporting_id + "' where user='"+str(request.user.username)+"'"
                mycursor.execute(query)
                mydb.commit()
        Blogs = Blog.objects.all()
    return render(request, 'maps_blog.html', {'flag': flag, 'blog_data': Blogs})

def display_blog_info(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    if (request.method=='GET'):
        # getting all the objects of Map
        Blogs = Blog.objects.all()
        return render(request, 'maps_blog.html', {'blog_data': Blogs})
    return redirect('/geofence/display_maps/')