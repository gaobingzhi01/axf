from django.conf.urls import url

from axf import views

urlpatterns = [
    url(r'^$', views.index),

    url(r'^home/$', views.home),
    url(r'^market/$', views.market),
    url(r'^cart/$', views.cart),
    url(r'^mine/$', views.mine),
]