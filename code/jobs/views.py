from django.shortcuts import render, redirect
from .models import *
from users.models import *
from accounts.models import *
# Create your views here.
def jobs(request):
	if 'email' in request.session:
		if JobsApplied.objects.filter(email=request.session['email']).exists():
			jobsapplied = JobsApplied.objects.filter(email=request.session['email']).values('job_id',
				'job_id__job_title', 'job_id__salary', 'job_id__job_role', 'job_id__experience_required',
				'job_id__job_type',)
			return render(request, 'jobs/jobsapplied.html', {'jobs':jobsapplied})
		else:
			return render(request, 'jobs/jobsapplied.html',{'message':"No jobs applied"})
	else:
		return redirect('/accounts/login')

def job_detail(request, job_id):
	job = Jobs.objects.get(job_id=job_id)
	if JobsApplied.objects.filter(email=request.session['email'], job_id=job_id).exists():
		message = "disable"
	else:
		message = "enable"
	return render(request, 'jobs/job_detail.html',{'job':job, 'message':message})

def apply(request, job_id):
	job = JobsApplied(email=UserDetails.objects.get(pk=request.session['email']),
		job_id=Jobs.objects.get(job_id=job_id))
	job.save()
	return redirect('/jobs/jobsapplied')

def dashboard(request):
	if 'email' in request.session:
		if TestsTaken.objects.filter(email=request.session['email']).exists():
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
			exclude_id = []
			jobs_exclude = JobsApplied.objects.filter(email=request.session['email'])
			for job in jobs_exclude:
				exclude_id.append(job.job_id)
			if Jobs.objects.filter(job_class=jc).exclude(job_title__in=exclude_id).exists():
				jobs = Jobs.objects.filter(job_class=jc).exclude(job_title__in = exclude_id)
				return render(request, 'jobs/dashboard.html',{'jobs':jobs})
			else:
				return render(request,'jobs/dashboard.html',{'message':"No jobs available right now"})
		else:
			message = "No Jobs loaded"
			return render(request, 'jobs/dashboard.html',{'message':message})
	else:
		return redirect('/accounts/login')

