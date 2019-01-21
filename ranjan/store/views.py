from django.db import connection
from django.shortcuts import render, redirect
from datetime import datetime

def check_if_auth_user(request):
    if request.session.has_key("user_mail_id"):
        return request.session["user_mail_id"]
    else:
        return None


'''def gallery(request):
    cursor= connection.cursor()
    cursor.execute ('select * from gallery_images')
    all_photos = cursor.fetchall()
    return render(request, 'gallery.html', {'all_photos':all_photos})'''


def display_store(request):
    cursor = connection.cursor()
    query = "select pid, name, description, imgurl, price from products;"
    cursor.execute(query)
    all_products = list(cursor.fetchall())

    if len(all_products) % 3 == 1:
        all_products.append(None)
        all_products.append(None)

    elif len(all_products) % 3 == 2:
        all_products.append(None)

    array = []

    x = 0

    for x in range(len(all_products)//3):
        val = 3*x
        temp = []
        temp.append(all_products[val])
        temp.append(all_products[val+1])
        temp.append(all_products[val+2])

        array.append(temp)

    print(array)
    return render(request, 'store.html',
                  {'isAuth': check_if_auth_user(request), 'array': array})


def productview(request, offset):
    if request.method == 'POST':

        # checking if logged in
        if not check_if_auth_user(request):
            return redirect('/accounts/login/') # if not logged in redirect to login

        else: # if logged in
            r_count = request.POST.get('count')
            r_bookfrom = request.POST.get('fromdate')
            r_booktill = request.POST.get('tilldate')
            r_productid = offset
            r_email = check_if_auth_user(request)

            date_format = "%Y-%m-%d"
            f = datetime.strptime(r_bookfrom, date_format)
            t = datetime.strptime(r_booktill, date_format)
            diff = t - f
            datediff = diff.days

            if r_productid and r_count and r_bookfrom and r_booktill and r_email and datediff >= 0:
                cursor = connection.cursor()
                insertquery = "Insert into cartdata (email, pid, fromdate, todate, count) values " \
                              "('" + r_email + "','" + r_productid + "', '" + r_bookfrom + "' , '" + r_booktill + "'," + r_count+ " );"
                try:
                    cursor.execute(insertquery)
                except Exception as e:
                    print(e, insertquery, '++++++++++++++')

                return redirect('/store/')

            else: # error page
                offset_val = offset
                cursor = connection.cursor()
                query = "select * from products where pid = '" + offset_val + "';"
                cursor.execute(query)
                result = cursor.fetchall()
                print('error', '*************')
                topresult = result[0]

                return render(request, 'productpage.html',
                              {'error': True, 'result': topresult, 'isAuth': check_if_auth_user(request)})

    # if request is get
    else:
        offset_val = offset
        cursor = connection.cursor()
        query = "select pid,name,description,imgurl,price,longdesc,delprice  from products where pid = '" + offset_val + "';"
        cursor.execute(query)
        result = cursor.fetchall()

        topresult = result[0]
        print('get', '******************')
        return render(request, 'productpage.html', {'result': topresult, 'isAuth': check_if_auth_user(request)})
