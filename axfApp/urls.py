from django.conf.urls import url

from axfApp import views

urlpatterns = [
    url(r'^index$', views.index),

    url(r'^home/$', views.home),
    url(r'^market/$', views.market),
    url(r'^cart/$', views.cart),
    url(r'^mine/$', views.mine),
]