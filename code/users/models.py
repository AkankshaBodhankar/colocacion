from django.db import models
from accounts.models import UserDetails

# Create your models here.
class Tests(models.Model):
	"""docstring for ClassName"""
	LEVELS=(
		('Easy','Easy'),
		('Medium','Medium'),
		('Difficult','Difficult'),
		)
	test_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=300, blank=False)
	level = models.CharField(max_length=10,choices=LEVELS)
	total_marks = models.IntegerField()
	def __str__(self):
		return self.title

class Questions(models.Model):
	CHOICE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
	test_id = models.ForeignKey(Tests, on_delete=models.CASCADE)
	question_id = models.IntegerField()
	title = models.CharField(max_length=1000)
	choice1 = models.CharField(max_length=200)
	choice2 = models.CharField(max_length=200)
	choice3 = models.CharField(max_length=200)
	choice4 = models.CharField(max_length=200)
	correct_choice = models.IntegerField(choices=CHOICE)
	def __str__(self):
	    return self.question_id

class Jobs(models.Model):
	job_id = models.AutoField(primary_key=True)
	job_title = models.CharField(max_length=300, blank=False)
	company_name = models.CharField(max_length=50, blank=False)
	salary = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
	desc = models.CharField(max_length=1000, blank=False)
	def __str__(self):
	    return self.job_id

class JobsApplied(models.Model):
	email = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
	job_id = models.ForeignKey(Jobs, on_delete=models.CASCADE)

class TestsTaken(models.Model):
	email = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
	test_id = models.ForeignKey(Tests, on_delete=models.CASCADE)

  