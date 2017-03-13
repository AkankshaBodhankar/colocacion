from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UserDetailsForm, UserProfileForm
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserDetails



# Create your views here.
def index(request):
	return render(request,'accounts/index.html')
        
def login(request):
    if request.method == 'POST':
        user = get_object_or_404(UserDetails, pk=request.POST['email'])
        if(user.password==request.POST['password']):
            request.session['email']=user.email
            return redirect('/jobs/dashboard/')
        else:
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        form1 = UserDetailsForm(request.POST,prefix="form1")
        form2 = UserProfileForm(request.POST,prefix="form2")
        if form1.is_valid() and form2.is_valid():
            userdetails = form1.save(commit=False)
            userprofile = form2.save(commit=False)
            userdetails.save()  
            userprofile.email = userdetails
            userprofile.save()
            messages.success(request, 'Successfully Registered! Sign in now!')
            return redirect('/accounts/login/')
    else:
        form1 = UserDetailsForm(prefix="form1")
        form2 = UserProfileForm(prefix="form2")
    return render(request, 'accounts/signup.html', {'form1': form1,'form2':form2})
