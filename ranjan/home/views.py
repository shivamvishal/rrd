from django.shortcuts import render

def check_if_auth_user(request):
    if request.session.has_key("user_mail_id"):
        return request.session["user_mail_id"]
    else:
        return None

def home(request):
    return render(request, 'rrd.html', {'isAuth': check_if_auth_user(request)})
