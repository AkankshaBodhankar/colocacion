from django import forms
from .models import UserDetails, UserProfile

class UserDetailsForm(forms.ModelForm):
	class Meta:
		password = forms.CharField(widget=forms.PasswordInput)
		model = UserDetails
		widgets = {
            'password': forms.PasswordInput(),
        }
		fields = ['email','name','password','city','mobile_num']	
        
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['college_name','branch','degree','degree_percent'
		,'inter_percent','ssc_percent','skills','interests' ]

		
			
		