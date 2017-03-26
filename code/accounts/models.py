from django.db import models
from django import forms

# Create your models here.
class UserDetails(models.Model):
	email = models.EmailField(max_length=200, primary_key=True, blank=False)
	name = models.CharField(max_length=200, blank=False)
	password = models.CharField(max_length=100)
	city = models.CharField(max_length=200)
	mobile_num = models.CharField(max_length=15)
	def __str__(self):
	    return self.email

class UserProfile(models.Model):
	DEGREE = (
        ('Btech', 'Btech'),
        ('Bcom', 'Bcom'),
        ('Bsc', 'Bsc'),
        ('Mtech', 'Mtech'),
        ('Msc', 'Msc'),
        ('BA','BA'),
        ('MBA','MBA'),
        ('BBA', 'BBA'),
    )
	email = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
	college_name = models.CharField(max_length=200)
	branch = models.CharField(max_length=15)
	degree = models.CharField(max_length=10, choices=DEGREE)
	degree_percent = models.CharField(max_length=5)
	inter_percent = models.CharField(max_length=5)
	ssc_percent = models.CharField(max_length=5)	
	skills = models.CharField(max_length=300)
	interests = models.CharField(max_length=300)
	def __str__(self):
	    return str(self.email)

class UserExperience(models.Model):
	email = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
	no_of_years = models.IntegerField()
	job_designation = models.CharField(max_length=100)
	keywords = models.CharField(max_length=300)
	def __str__(self):
	    return self.email
