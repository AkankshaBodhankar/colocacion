from django.shortcuts import render, redirect
from .models import *
from users.models import *
from accounts.models import *
# Create your views here.
def jobs(request):
	if 'email' in request.session:
		if JobsApplied.objects.filter(email=request.session['email']).exists():
			jobsapplied = JobsApplied.objects.filter(email=request.session['email'])
			return render(request, 'jobs/jobsapplied.html', {'jobs':jobsapplied})
		else:
			return render(request, 'jobs/jobsapplied.html',{'message':"No jobs applied"})
	else:
		return redirect('/accounts/login')

def job_detail(request, job_id):
	job = Jobs.objects.get(job_id=job_id)
	return render(request, 'jobs/job_detail.html',{'job':job})

def apply(request, job_id):
	job = JobsApplied(email=UserDetails.objects.get(pk=request.session['email']),
		job_id=Jobs.objects.get(job_id=job_id))
	job.save()
	return redirect('/jobs/jobsapplied')

def dashboard(request):
	if 'email' in request.session:
		teststaken = TestsTaken.objects.filter(email=request.session['email'])
		jc = 'C'
		marks = 0
		count = 0
		for test in teststaken:
			marks = marks+test.marks_obtained
			count = count + 1
		avg = (marks/count)*100
		if avg>=75:
			jc = 'A'
		elif avg>=45 and avg<=50:
			jc = 'B'
		jobs = Jobs.objects.filter(job_class=jc)
		return render(request, 'jobs/dashboard.html',{'jobs':jobs})
	else:
		return redirect('/accounts/login')

