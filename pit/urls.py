from django.conf.urls import url
from . import views
from . import views_kkb

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^transactions$', views.kzt_list, name='kzt_list'),
    url(r'^success$', views.success, name='success'),
    url(r'^transactions/new/$', views.transaction_new, name='transaction_new'),
    url(r'^dog/new/$', views.dog_new, name='dog_new'),
    url(r'^donate$', views_kkb.kkb_init, name='kkb_init'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]
