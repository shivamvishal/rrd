from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^adminlogin/$', views.adminlogin, name="admin login"),
    url(r'^adminlogout/$', views.adminlogout, name="admin logout"),
    url(r'^addproduct/$', views.addproduct, name="add product"),
    url(r'^updateproduct/(\w+)/$', views.updateproduct, name="add product"),
    url(r'^addgalleryimg/$', views.addgalleyimage, name="add to gallery"),
    url(r'^delgalleryimg/(\d+)/$', views.delgalleryimage, name="add to gallery"),
    url(r'^productstable/$', views.productstable, name="add to gallery"),
    url(r'^gallerytable/$', views.gallerytable, name="add to gallery"),
    url(r'^customertable/$', views.gallerytable, name="add to gallery"),
]
