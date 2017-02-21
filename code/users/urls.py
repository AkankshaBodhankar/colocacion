from django.conf.urls import url, include
from . import views

urlpatterns = [

     url(r'^profile/$', views.profile, name='profile'),
     url(r'^profileedit/$', views.profileedit, name='profileedit'),
     url(r'^tests/$', views.tests, name='tests'),
     url(r'^dashboard/$', views.dashboard, name='dashboard'),
     url(r'^jobs/$', views.jobs, name='jobs'),
]
