
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^load_form$', views.load_form),
    url(r'^add$', views.add),
    url(r'^show$', views.show),  
    url(r'^edit/(?P<id>\d+)/$', views.edit), 
    url(r'^update/(?P<id>\d+)$', views.update), 
    url(r'^delete/(?P<id>\d+)$', views.delete), 
    url(r'^search$', views.search), 
]
