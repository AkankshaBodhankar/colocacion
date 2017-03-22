from django.shortcuts import render, redirect
from .models import *
from users.models import *
from accounts.models import *
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy import spatial

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
	#content based algorithm
	applied = False
	if JobsApplied.objects.filter(email=request.session['email']):
		applied = True
		jobs_exclude = JobsApplied.objects.filter(email=request.session['email'])
		exclude_id = []
		for job in jobs_exclude:
			exclude_id.append(job.job_id)
		df = pd.DataFrame(list(Jobs.objects.all().values()))
		df_exclude = pd.DataFrame(list(jobs_exclude.values()))
		cvCompName = CountVectorizer()
		cvDesc =CountVectorizer()
		cvJobClass = CountVectorizer()
		cvJobRole = CountVectorizer()
		cvJobTitle = CountVectorizer()
		cvJobType = CountVectorizer()
		cvLocation = CountVectorizer()
		cvSkills = CountVectorizer()
		
		cvCompNameVal = cvCompName.fit_transform(df["company_name"].tolist())
		cvDescVal=cvDesc.fit_transform(df["desc"].tolist())
		cvJobRoleVal = cvJobRole.fit_transform(df["job_role"].tolist())
		cvJobTitleVal = cvJobTitle.fit_transform(df["job_title"].tolist())
		cvJobTypeVal = cvJobType.fit_transform(df["job_type"].tolist())
		cvLocationVal = cvLocation.fit_transform(df["location"].tolist())
		cvSkillsVal = cvSkills.fit_transform(df["skills_set"].tolist())
		salary=df["salary"].values
		salary=salary/float(max(salary))
		salary=salary.reshape(len(salary),1)
		experience=df["experience_required"].values
		experience=experience/float(max(experience))
		experience=experience.reshape(len(experience),1)
		finalnp=list(np.concatenate((cvCompNameVal.toarray(), cvDescVal.toarray(),cvJobRoleVal.toarray(),
			cvJobTitleVal.toarray(),cvJobTypeVal.toarray(),cvLocationVal.toarray(),cvSkillsVal.toarray(),salary,experience), axis=1))
		
		df_applied = pd.DataFrame(list(JobsApplied.objects.filter(email=request.session['email']).values('job_id',
					'job_id__company_name', 'job_id__desc', 'job_id__job_role', 'job_id__job_title', 
					'job_id__job_type','job_id__location','job_id__skills_set','job_id__salary','job_id__experience_required')))
		
		cvCompNameUser = cvCompName.transform(df_applied["job_id__company_name"].tolist())
		cvDescUser=cvDesc.transform(df_applied["job_id__desc"].tolist())
		cvJobRoleUser = cvJobRole.transform(df_applied["job_id__job_role"].tolist())
		cvJobTitleUser = cvJobTitle.transform(df_applied["job_id__job_title"].tolist())
		cvJobTypeUser = cvJobType.transform(df_applied["job_id__job_type"].tolist())
		cvLocationUser = cvLocation.transform(df_applied["job_id__location"].tolist())
		cvSkillsUser = cvSkills.transform(df_applied["job_id__skills_set"].tolist())
		salaryUser=df_applied["job_id__salary"].values
		salaryUser=salaryUser/float(max(salaryUser))
		salaryUser=salaryUser.reshape(len(salaryUser),1)
		experienceUser=df_applied["job_id__experience_required"].values
		experienceUser=experienceUser/float(max(experienceUser))
		experienceUser=experienceUser.reshape(len(experienceUser),1)

		finalnpUser=list(np.concatenate((cvCompNameUser.toarray(), cvDescUser.toarray(),cvJobRoleUser.toarray(),
			cvJobTitleUser.toarray(),cvJobTypeUser.toarray(),cvLocationUser.toarray(),cvSkillsUser.toarray(),salaryUser,experienceUser), axis=1))
		
		similarity=np.array([[1-spatial.distance.cosine(i,j) for j in finalnp] for i in finalnpUser])
		exc=list(df_exclude["job_id_id"].values)
		scores=np.sum(similarity,axis=0)
		predictions=list(reversed(np.argsort(scores)))
		predictions=[i+1 for i in predictions]
		finalpred=[i for i in predictions if i not in exc]
		jobs = Jobs.objects.filter(job_id__in=finalpred[:5])
	    
    #filtering by test results
	if TestsTaken.objects.filter(email=request.session['email']).exists():
		teststaken = TestsTaken.objects.filter(email=request.session['email'])
		jc = 'C'
		marks = 0
		count = 0
		for test in teststaken:
			marks = marks + test.marks_obtained
			count = count + 1
		avg = (marks/count)
		if avg>=75:
			jc = 'A'
		elif avg>=45 and avg<=50:
			jc = 'B'
		if applied:
			finaljobs = Jobs.objects.filter(job_class = jc, job_id__in = jobs)
			return render(request, 'jobs/dashboard.html',{'jobs':finaljobs})
		else:
			exclude_id = []
			jobs_exclude = JobsApplied.objects.filter(email=request.session['email'])
			for job in jobs_exclude:
				exclude_id.append(job.job_id)
			if Jobs.objects.filter(job_class=jc).exclude(job_title__in=exclude_id).exists():
				jobs = Jobs.objects.filter(job_class=jc).exclude(job_title__in = exclude_id)
			return render(request, 'jobs/dashboard.html',{'jobs':jobs})
	else:
		return render(request,'jobs/dashboard.html',{'message':"No jobs available right now"})
