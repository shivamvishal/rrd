from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.display_store, name="view store"),
    url(r'^productview/(\w+)/$', views.productview, name="view store"),
]

