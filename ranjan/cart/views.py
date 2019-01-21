from django.shortcuts import render, redirect
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime



def check_if_auth_user(request):
    if request.session.has_key("user_mail_id"):
        return request.session["user_mail_id"]
    else:
        return None





def getdata1(user_email):
    cursor = connection.cursor()
    query = "SELECT cartdata.email, cartdata.pid, cartdata.fromdate, cartdata.todate, cartdata.count, products.name, products.imgurl, products.price, products.delprice FROM cartdata,products WHERE cartdata.email= %s AND cartdata.pid = products.pid;"
    cursor.execute(query, [user_email])
    data = cursor.fetchall()
    return list(data)



@csrf_exempt
def display_cart(request):
    user_email = check_if_auth_user(request)
    if request.method == 'GET':
        if not user_email:  # if user is not logged in redirect to login
            return redirect('/accounts/login')

        else:
            data = getdata1(user_email)
            if data:
                zip = []
                net = []
                subtotal = 0
                shipping = 0
                for x in range(len(data)):
                    datefrom, dateto = str(data[x][2]), str(data[x][3])

                    date_format = "%Y-%m-%d"
                    f = datetime.strptime(datefrom, date_format)
                    t = datetime.strptime(dateto, date_format)
                    diff = t - f
                    datediff = diff.days

                    netprice = int(data[x][4]) * int(data[x][7]) * int(datediff)
                    subtotal += netprice
                    shipping += int(data[x][4]) * int(data[x][8])

                    temp = [data[x], netprice, datefrom, dateto]
                    zip.append(temp)

                finalcost = subtotal + shipping
                return render(request, 'cart.html',
                              {'zip': zip, 'subtotal': subtotal, 'shipping': shipping, 'finalcost': finalcost,
                               'isAuth': check_if_auth_user(request)})
            else:
                return render(request, 'cart.html', {'empty': True, 'isAuth': check_if_auth_user(request)})

    else:  # post
        # hamko chahiye email, pid, locality, city, pin, from, to, count
        # locality, city, pin form se nikalo
        # email, pid, from, to, count isi page me milega
        r_email = user_email
        r_cost = request.POST.get('ficost')
        r_city = request.POST.get('city')
        r_locality = request.POST.get('locality')
        r_pin = request.POST.get('pincode')
        if r_email and r_pin and r_city and r_locality:
            cursor1 = connection.cursor()
            cursor2 = connection.cursor()
            addaddressquerry = "insert into address (email, locality, city, pin) values ('" + r_email + "','" + r_locality + "','" + r_city + "','" + r_pin + "');"
            cursor1.execute(addaddressquerry)
            fetchaddressquery = "select addid from address where locality = '" + r_locality + "' and  city='" + r_city + "' and pin ='" + r_pin + "';"
            cursor1.execute(fetchaddressquery)
            addid = cursor1.fetchone()
            addid = addid[0]

            fetchcartdata = "select * from cartdata where email = '" + user_email + "';"
            cursor2.execute(fetchcartdata)
            cartdata = list(cursor2.fetchall())
            print('*****************************')
            addtodeliquery = ""
            for item in cartdata:
                rec_email = item[0]
                rec_pid = item[1]
                rec_fromdate = str(item[2])
                rec_todate = str(item[3])
                rec_count = str(item[4])

                # add into delivery table
                # print(rec_email,rec_pid,rec_fromdate,rec_todate,rec_count,'+++++++++++++++++++++++++++')
                addtodeliquery = "insert into delivery (email, pid, fromdate, todate, count, addid) values ('" + user_email + "','" + rec_pid + "','" + rec_fromdate + "','" + rec_todate + "'," + rec_count + "," + str(
                    addid) + ");"
                # print( '///////////////////////********////////////')
                cursor2.execute(addtodeliquery)

            # deleting from cart
            deletequery = "delete from cartdata where email='" + user_email + "';"
            cursor2.execute(deletequery)
            return render(request, 'success.html',{'cost': r_cost})
        else:
            return render(request, 'cart.html', {'isAuth': check_if_auth_user(request)})


def removeitem(request, offset):
    email, pid, fromdate, todate = offset.strip().split('+')
    cursor = connection.cursor()
    query = "delete from cartdata where email = '" + email + "'and pid ='" + pid + "' and fromdate = '" + fromdate + "' and todate = '" + todate + "';"
    cursor.execute(query)
    return redirect('/cart/')


def makepayment(request, offset):
    email, pid, fromdate, todate = offset.strip().split('+')
    cursor = connection.cursor()
    delquery = "insert into delivery (email, pid, fromdate, todate, count, )"
    query = "delete from cartdata where email = '" + email + "'and pid ='" + pid + "' and fromdate = '" + fromdate + "' and todate = '" + todate + "';"
    cursor.execute(query)
    return redirect('/cart/')
