from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['first_name','last_name','email','username','password']
		label = {'password':'Password'}

	def __init__(self,*args,**kwargs):
		if kwargs.get('instance'):
			initial = kwargs.setdefault('initial',{})
			if kwargs['instance'].groups.all():
				initial['role'] = kwargs['instance'].groups.all()[0]
			else:
				initial['role'] = None
		forms.ModelForm.__init__(self,*args,**kwargs)

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


