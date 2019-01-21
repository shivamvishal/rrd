from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name="login1"),
    url(r'^logout/$', views.user_logout, name="logout"),
    url(r'^register/$', views.user_registration, name="register"),
]
