from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db import connection

from .models import Images


def check_if_auth_user(request):
    if request.session.has_key("user_mail_id"):
        return request.session["user_mail_id"]
    else:
        return None


def gallery(request):
    cursor = connection.cursor()
    query = "select * from gallerydata;"
    cursor.execute(query)
    all_photos = cursor.fetchall()
    return render(request, 'gallery.html', {'all_photos': all_photos, 'isAuth': check_if_auth_user(request)})


