from django.db import models
from accounts.models import UserDetails

# Create your models here.
class Jobs(models.Model):
	JOBCLASS=(
		('A','A'),
		('B','B'),
		('C','C'),
		)
	job_id = models.AutoField(primary_key=True)
	job_role = models.CharField(max_length=500)
	job_title = models.CharField(max_length=300, unique=True, blank=False)
	job_type = models.CharField(max_length=100)
	experience_required = models.IntegerField()
	company_name = models.CharField(max_length=50, blank=False)
	salary = models.IntegerField(blank=False)
	location = models.CharField(max_length=500)
	skills_set = models.CharField(max_length=1000)
	job_class = models.CharField(max_length=1, choices=JOBCLASS)
	desc = models.TextField(blank=False)
	def __str__(self):
	    return (self.job_title)

class JobsApplied(models.Model):
	email = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
	job_id = models.ForeignKey(Jobs, on_delete=models.CASCADE)
	def __str__(self):
	    return str(self.job_id)
