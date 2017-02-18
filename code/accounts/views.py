from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UserDetailsForm

# Create your views here.
def index(request):
	return render(request,'accounts/index.html')

def login(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('/accounts/login/')
    else:
        form = UserDetailsForm()
    return render(request, 'accounts/login.html', {'form': form})
