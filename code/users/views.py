from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from accounts.models import *
from accounts.forms import *
from users.models import *
from django.http import Http404
from django.contrib import messages
from django.urls import reverse

def profile(request):
	if 'email' in request.session:
		userdetails = UserDetails.objects.get(email=request.session['email'])
		userprofile = UserProfile.objects.get(email=request.session['email'])
		return render(request, 'users/profile.html', {'form1':userdetails, 'form2':userprofile})
	if request.method == 'POST':
		userdetails = UserDetails.objects.get(email=request.session['email'])
		if(userdetails.password==request.POST['oldpwd'] and request.POST['newpwd']==request.POST['retypenewpwd']):
			userdetails.password = request.POST['newpwd']
			userdetails.save()
			messages.success(request, "Changed password successfully!")
			return redirect('/users/profile')
	else:
		return redirect('/accounts/login')

def profileedit(request):
	if 'email' in request.session:
		userdetails = UserDetails.objects.get(email=request.session['email'])
		request.session['password'] = userdetails.password
		userprofile = UserProfile.objects.get(email=request.session['email'])
		if request.method == 'POST':
			form1 = UserDetailsForm(request.POST, instance=userdetails)
			form2 = UserProfileForm(request.POST, instance= userprofile)
			if form1.is_valid() and form2.is_valid():
				userdetails = form1.save(commit=False)
				userprofile = form2.save(commit=False)
				userdetails.email = request.session['email']
				if(userdetails.password==request.session['password']):
					userdetails.save()
					userprofile.email = userdetails
					userprofile.save()
					return redirect('/users/profile')
				else:
					messages.error(request, "Wrong password")
		else:
			form1 = UserDetailsForm(instance=userdetails)
			form2 = UserProfileForm(instance=userprofile)
		return render(request,'users/profileedit.html',{'form1':form1,'form2':form2})
	else:
		return redirect('/accounts/login')

def tests(request):
	if 'email' in request.session:
		if TestsTaken.objects.filter(email=request.session['email']).exists():
			teststaken = TestsTaken.objects.filter(email=request.session['email']).values('test_id','marks_obtained'
				,'test_id__level','test_id__total_marks','test_id__title')
			return render(request, 'users/tests.html', {'tests':teststaken})
		else:
			return render(request, 'users/tests.html',{'message':"No tests taken"})
	else:
		return redirect('/accounts/login')

def taketests(request, tlevel):
	test = get_object_or_404(Tests, level=tlevel)
	if TestsTaken.objects.filter(email=request.session['email'], test_id=test.test_id).exists():
		teststaken = TestsTaken.objects.filter(email=request.session['email']).values('test_id','marks_obtained'
				,'test_id__level','test_id__total_marks','test_id__title')
		messages.error(request, 'Test already taken')
		return render(request,'users/tests.html',{'tests':teststaken})
	else:
		question = Questions.objects.get(test_id=test.test_id, question_id=1)
		request.session['marks'] = 0
		return render(request, 'users/taketests.html', {'question':question, 'test':test})

def question(request, testid, questionid):
	if 'marks' in request.session:
		test = get_object_or_404(Tests, test_id=testid)
		if Questions.objects.filter(test_id=testid, question_id=questionid).exists():
			question = Questions.objects.get(test_id=testid, question_id=questionid)
			nques = int(questionid)+1
			return render(request, 'users/question.html', {'test':test, 'question':question, 'next':nques})
		else:
			marks = int(request.session['marks'])
			del request.session['marks']
			p = TestsTaken(email=UserDetails.objects.get(pk=request.session['email']), 
				test_id=Tests.objects.get(test_id=testid), marks_obtained=marks)
			p.save()
			return render(request, 'users/results.html', {'test':test, 'marks': marks})

def results(request):
	if 'marks' not in request.session:
		return redirect('/users/tests')
	else:
		return redirect('/users/tests')

def countmarks(request, test_id, question_id):
	if Questions.objects.filter(test_id=test_id, question_id=question_id).exists():
	    question = get_object_or_404(Questions, test_id=test_id, question_id=question_id)
	    try:
	        selected_choice = question.choice_set.get(pk=request.POST['choice'])
	    except (KeyError, Choice.DoesNotExist):
	      	        return render(request, 'users/taketests.html', {
	            'question': question,
	            'error_message': "You didn't select a choice.",
	        })
	    else:
	        if str(selected_choice) == str(question.correct_choice):
	        	noq = Questions.objects.filter(test_id=test_id).count()
	        	test = Tests.objects.get(test_id=test_id)
	        	request.session['marks'] = request.session['marks'] + (test.total_marks/noq)
	        ans = Answers(email=UserDetails.objects.get(pk=request.session['email']),
	        	test_id=Tests.objects.get(test_id=test_id), question_id=Questions.objects.get(test_id=test_id,
	        		question_id=question_id),choice_id_selected=str(selected_choice.choice_text))
	        ans.save()
	        nques = int(question_id)+1
	        return redirect('/users/question/'+str(test_id)+'/'+str(nques))
	else:
		return redirect('/users/results')

def answers(request, test_id):
	if 'email' in request.session and TestsTaken.objects.filter(email=request.session['email'],
		test_id=test_id).exists():
		test = TestsTaken.objects.filter(email=request.session['email'], test_id=test_id).values('test_id','marks_obtained'
				,'test_id__level','test_id__total_marks','test_id__title')
		question = Questions.objects.filter(test_id=test_id)
		answers = Answers.objects.filter(email=request.session['email'], test_id=test_id).values(
			'question_id','choice_id_selected','question_id__question_text','question_id__correct_choice'
			)
		return render(request,'users/answers.html',{'answers':answers, 'tests':test, 'questions':question})
	else:
		return redirect('/users/tests')

def logout(request):
	if 'email' in request.session:
		try:
			del request.session['email']
		except KeyError:
			pass
		return redirect('/accounts/login')
