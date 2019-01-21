from django.db import models

# Create your models here.


def start_user_session(request, user_id, user_class):
    request.session["user_mail_id"] = user_id
    request.session["user_class"] = user_class
    return request


def check_if_auth_user(request):
    if request.session.has_key("user_mail_id"):
        return request.session["user_mail_id"]
    else:
        return None


def stop_user_session(request):
    if request.session.has_key("user_mail_id"):
        del request.session["user_mail_id"]
        del request.session["user_class"]
        return True
    return False