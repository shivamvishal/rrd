import os
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import connection
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import base64
from .models import *
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

mediafile_location = os.path.join(BASE_DIR, 'media/')


# gallery.....................................................
def addgalleyimage(request):
    if request.method == 'POST' and request.FILES["image"]:
        myfile = request.FILES["image"]
        title = request.POST.get('title')
        filename = myfile.name
        print(filename, title, type(myfile), "hahahahahh")

        photo = myfile.read()
        pic64 = base64.encodestring(photo)

        # insert into media file
        try:
            file = open(mediafile_location + filename, 'wb')
            file.write(photo)
        except Exception as e:
            print(e, 'file not written ++++++++++++++')

        # insert into database
        try:
            cursor = connection.cursor()
            insertquery = "insert into gallerydata ( image, title, filename) values (%s, %s, %s);"
            cursor.execute(insertquery, [pic64, title, filename])
        except Exception as e:
            print(e, 'error inserting into database')

        return render(request, 'myadmin/addgallery.html', {'success': True})

    else:
        return render(request, 'myadmin/addgallery.html')


def delgalleryimage(request,offset):
    cursor = connection.cursor()
    delquery = "delete from gallerydata where imgid = %s;"
    cursor.execute(delquery,[offset])
    return redirect('/myadmin/gallerytable/')


# gallery end ...........................................


# product ................................................
def addproduct(request):
    if check_if_auth_user(request):
        if request.method == 'POST' and request.FILES["image"]:
            myfile = request.FILES["image"]

            pid = request.POST.get('pid')
            name = request.POST.get('name')
            description = request.POST.get('description')
            filename = myfile.name
            price = int(request.POST.get('price'))
            longdesc = request.POST.get('longdesc')
            delprice = int(request.POST.get('delprice'))
            type1 = request.POST.get('type')



            photo = myfile.read()
            pic64 = base64.encodestring(photo)

            # insert into media file
            mediafile_location = os.path.join(BASE_DIR, 'media/media/')
            try:
                file = open(mediafile_location + filename, 'wb')
                file.write(photo)
            except Exception as e:
                print(e, 'file not written ++++++++++++++')

            # insert into database
            try:
                cursor = connection.cursor()
                insertquery = "insert into products (pid, name, description, imgurl, price, longdesc, delprice, productimage, type) values (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

                cursor.execute(insertquery, [pid, name, description, filename, price, longdesc, delprice, pic64, type1])
            except Exception as e:
                print(e, 'error inserting into database')

            return render(request, 'myadmin/addproduct.html', {'success': True, 'isAuth': check_if_auth_user(request)})

        else:
            return render(request, 'myadmin/addproduct.html', {'pagename': 'Add Product', 'isAuth': check_if_auth_user(request)})

    else:
        return render(request, 'forbidden.html')


def updateproduct(request, offset):
    if request.method == 'POST':
        pass


    else:
        return render(request,'myadmin/addproduct.html',{'UpdateMode': True, 'pid': offset})



# products end.....................

# tables ...............................
def productstable(request):
    if check_if_auth_user(request):
        cursor = connection.cursor()
        query = "select pid,name,description,imgurl,price,longdesc,delprice,type from products;"
        cursor.execute(query)
        data = cursor.fetchall()

        return render(request, 'myadmin/productstable.html', {'data': data, 'tablename': 'Products'})

    else:
        return render(request, 'forbidden.html')

def gallerytable(request):
    if check_if_auth_user(request):
        cursor = connection.cursor()
        query = "select imgid,title,filename from gallerydata;"
        cursor.execute(query)
        data = cursor.fetchall()

        return render(request, 'myadmin/gallerytable.html', {'data': data})

    else:
        return render(request, 'forbidden.html')





# tables end ...............................


# login .......................
def adminlogin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        print(name, password, '++++++++++++++++++++')
        if name == 'cyberbeast' and password == "cyberbeast":
            start_user_session(request, name, 'S')
            return HttpResponseRedirect('/myadmin/addproduct/')

        else:
            return render(request, 'myadmin/adminlogin.html', {'error': True})

    else:
        return render(request, 'myadmin/adminlogin.html')


def adminlogout(request):
    stop_user_session(request)
    return redirect('/myadmin/adminlogin/')
# longin end..........................................