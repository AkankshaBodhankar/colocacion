from django import forms
from .models import UserDetails

class UserDetailsForm(forms.ModelForm):
	class Meta:
		password = forms.CharField(widget=forms.PasswordInput)
		model = UserDetails
		widgets = {
            'password': forms.PasswordInput(),
        }
		fields = ['email','name','password','city','mobile_num']	
        
		