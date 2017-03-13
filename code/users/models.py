from django.db import models
from accounts.models import UserDetails

class Tests(models.Model):
	LEVELS=(
		('easy','easy'),
		('medium','medium'),
		('difficult','difficult'),
		)
	test_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=300, blank=False)
	level = models.CharField(max_length=10,choices=LEVELS)
	total_marks = models.IntegerField()
	def __str__(self):
		return self.title

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
	marks_obtained = models.IntegerField(default=0)

class Questions(models.Model):
	class Meta:
		unique_together = (("test_id","question_id"),)
	test_id = models.ForeignKey(Tests, on_delete=models.CASCADE)
	question_id = models.IntegerField()
	question_text = models.CharField(max_length=1000)
	correct_choice = models.CharField(max_length=1000)
	def __str__(self):
	    return str(self.question_text)

class Choice(models.Model):
	class Meta:
		unique_together = (("test_id","question_id","choice_id"),)
	test_id = models.ForeignKey(Tests, on_delete=models.CASCADE)
	question_id = models.ForeignKey(Questions, on_delete=models.CASCADE,)
	choice_id = models.IntegerField()
	choice_text = models.CharField(max_length=1000)
	def __str__(self):
	    return self.choice_text
  