from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.ForeignKey(User)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pin = models.IntegerField()
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'accounts'

    def __unicode__(self):
        return u"%s" % self.name

    @models.permalink
    def get_absolute_url(self):
        return 'account_detail', [self.uuid]

    @models.permalink
    def get_update_url(self):
        return 'account_update', [self.uuid]

    @models.permalink
    def get_delete_url(self):
        return 'account_delete', [self.uuid]


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
