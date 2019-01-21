from django.shortcuts import render



def check_if_auth_user(request):
    if request.session.has_key("user_mail_id"):
        return request.session["user_mail_id"]
    else:
        return None

def contact(request):
    return render(request, 'contact.html',{'isAuth': check_if_auth_user(request)})
