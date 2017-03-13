from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from accounts.models import *
from accounts.forms import *
from users.models import *
from django.contrib import messages
from django.urls import reverse

def profile(request):
	if 'email' in request.session:
		userdetails = UserDetails.objects.get(email=request.session['email'])
		userprofile = UserProfile.objects.get(email=request.session['email'])
		return render(request, 'users/profile.html', {'form1':userdetails, 'form2':userprofile})
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
			teststaken = TestsTaken.objects.filter(email=request.session['email'])
			return render(request, 'users/tests.html', {'tests':teststaken})
		else:
			return render(request, 'users/tests.html',{'message':"No tests taken"})
	else:
		return redirect('/accounts/login')

def taketests(request, tlevel):
	test = get_object_or_404(Tests, level=tlevel)
	if TestsTaken.objects.filter(email=request.session['email'], test_id=test.test_id).exists():
		teststaken = TestsTaken.objects.filter(email=request.session['email'])
		messages.error(request, 'Test already taken')
		return render(request,'users/tests.html',{'tests':teststaken})
	else:
		question = Questions.objects.get(test_id=test.test_id, question_id=1)
		request.session['marks'] = 0
		return render(request, 'users/taketests.html', {'question':question, 'test':test})

def question(request, testid, questionid):
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
	return HttpResponse("This is results page!")

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
	        nques = int(question_id)+1
	        return redirect('/users/question/'+str(test_id)+'/'+str(nques))
	else:
		return redirect('/users/results')

def logout(request):
	if 'email' in request.session:
		try:
			del request.session['email']
		except KeyError:
			pass
		return redirect('/accounts/login')
