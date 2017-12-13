from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='kzt_list'),
    url(r'^transactions$', views.kzt_list, name='kzt_list'),
]
