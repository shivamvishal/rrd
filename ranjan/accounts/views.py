from django.contrib import messages
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import social.apps.django_app.default.models as sm

from .models import start_user_session, stop_user_session, check_if_auth_user
import hashlib

salt = 'i am the key'.encode('utf-8')

def user_login(request):
    next = request.GET.get('next', '/home/')
    context = RequestContext(request)
    if request.method == 'POST':
        rec_email = request.POST.get('email')
        rec_password = request.POST.get('password')

        context_data = {}

        rec_password = rec_password.encode('utf-8')
        var2 = hashlib.sha256(rec_password + salt).hexdigest()


        if rec_password and rec_email:
            cursor = connection.cursor()
            query = "SELECT email, password, firstname FROM Customer where email ='" + rec_email + "'and password = '" + var2 + "' ;"
            cursor.execute(query)
            result = cursor.fetchall()

            print(len(result), '///////////////////////////////////')
            error = False
            if result:
                messages.success(request, "successful login")
                request = start_user_session(request, rec_email, 'E')
                return redirect("/home/")

            else:
                error = True
                return render(request, 'form-login.html', {'error': error})
    else:
        return render(request, 'form-login.html', {'isAuth': check_if_auth_user(request)})


def user_logout(request):
    stop_user_session(request)
    return HttpResponseRedirect('/home/')

@csrf_exempt
def user_registration(request):
    if request.method == 'POST':
        r_firstname = request.POST.get('form-first-name')
        r_lastname = request.POST.get('form-last-name')
        r_phone = request.POST.get('form-mobile')
        r_email = request.POST.get('form-email')
        r_password = request.POST.get('form-password')
        r_address = request.POST.get('form-street')
        r_city = request.POST.get('form-city')
        r_pincode = request.POST.get('form-pincode')

        r_password = r_password.encode('utf-8')
        var1 = hashlib.sha256(r_password + salt).hexdigest()

        if r_password and r_email and r_phone and r_firstname and r_lastname and r_address and r_city and r_pincode:
            cursor = connection.cursor()
            query = "INSERT INTO CUSTOMER(" \
                    "email, firstname, lastname, password, phone, address, city, pin ) values " \
                    "( '" + r_email + "' ,'" + r_firstname + "' ,'" + r_lastname + "' ,'" + var1 + "' ,'" + r_phone + "' ,'" + r_address + "' ,'" + r_city + "' ,'" + r_pincode + "');"
            try:
                cursor.execute(query)
                insert_status = True
            except Exception as e:
                insert_status = False
                print(e, "error inserting into database")

            print('///////////////////////////////////')

            if insert_status:
                messages.success(request, "successful registration")
                messages.success(request, "logging in")
                request = start_user_session(request, r_email, 'E')
                return redirect("/home/")

            else:
                error = True
                return render(request, 'register.html', {'error': error})
    else:
        return render(request, 'register.html')
