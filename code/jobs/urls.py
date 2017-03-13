from django.conf.urls import url, include
from . import views

urlpatterns = [
     url(r'^jobsapplied/$', views.jobs, name='jobsapplied'),
     url(r'^dashboard/$', views.dashboard, name='dashboard'),
     url(r'^job_detail/(?P<job_id>\d+)/$', views.job_detail, name='job_detail'),
     url(r'^apply/(?P<job_id>\d+)/$', views.apply, name="apply"),
]
