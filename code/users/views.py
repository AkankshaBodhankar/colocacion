from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import UserDetails, UserProfile
from accounts.forms import UserDetailsForm, UserProfileForm
from django.contrib import messages

# Create your views here.
def profile(request):
	if(request.session['email'] is not None):
		userdetails = UserDetails.objects.get(email=request.session['email'])
		userprofile = UserProfile.objects.get(email=request.session['email'])
		return render(request, 'users/profile.html', {'form1':userdetails, 'form2':userprofile})

def profileedit(request):
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

def tests(request):
	return render(request, 'users/tests.html')

def dashboard(request):
	return render(request, 'users/dashboard.html')

def jobs(request):
	return render(request, 'users/jobs.html')
