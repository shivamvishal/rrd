from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.display_cart, name="display cart"),
    url(r'^remove/(.+)$', views.removeitem, name="remove item from cart"),
    # url(r'^productview/(\w+)/$', views.productview, name="view store"),
]


