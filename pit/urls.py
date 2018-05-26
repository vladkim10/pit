from django.conf.urls import url
from . import views
from . import views_kkb

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pets/(?P<pet_type>[a-z]+)/$', views.pets_view, name='pets'),
    url(r'^pets/(?P<pet_type>[a-z]+)/new/$', views.pet_new, name='pet_new'),
    url(r'^morepet/(?P<pk>\d+)/$', views.morepet, name='morepet'),
    url(r'^pet/(?P<pk>\d+)/delete$', views.delete_pet, name='delete_pet'),
    url(r'^pet/hidden/$', views.hidden_pet, name='hidden_pet'),
    url(r'^pet/(?P<pk>\d+)/return$', views.return_pet, name='return_pet'),
    url(r'^transactions$', views.kzt_list, name='kzt_list'),
    url(r'^success$', views.success, name='success'),
    url(r'^transactions/new/$', views.transaction_new, name='transaction_new'),
    url(r'^donate$', views_kkb.kkb_init, name='kkb_init'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^client/$', views.client, name='client'),
    url(r'^client/(?P<pk>\d+)/delete$', views.delete_client, name='delete_client'),
    url(r'^client/hidden/$', views.hidden_client, name='hidden_client'),
    url(r'^client/(?P<pk>\d+)/return$', views.return_client, name='return_client'),
    url(r'^pet/(?P<pk>\d+)/client/new/$', views.client_new, name='client_new'),
    url(r'^client/new/thanks$', views.thanks, name='thanks'),
    url(r'^condition/$', views.condition, name='condition'),
    url(r'^pets/new/success/$', views.pet_success, name='pet_success'),
]
