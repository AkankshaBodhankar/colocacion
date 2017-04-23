from django.conf.urls import url, include
from . import views

urlpatterns = [

     url(r'^profile/$', views.profile, name='profile'),
     url(r'^profileedit/$', views.profileedit, name='profileedit'),
     url(r'^tests/$', views.tests, name='tests'),
     url(r'^taketests/(?P<tlevel>[a-z]+)/$', views.taketests, name='taketests'),
     url(r'^countmarks/(?P<test_id>[0-9]+)/(?P<question_id>[0-9]+)/$', views.countmarks, name='countmarks'),
     url(r'^question/(?P<testid>[0-9]+)/(?P<questionid>[0-9]+)/$', views.question, name='question'),
     url(r'^results/$', views.results, name="results"),
     url(r'^answers/(?P<test_id>[0-9]+)/$', views.answers, name="answers"),
     url(r'^logout/$', views.logout, name="logout"),
     url(r'^changepassword/$', views.changepassword, name="changepassword"),
]
