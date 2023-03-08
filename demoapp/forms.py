from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput

from demoapp.models import Login, userlogin, eventadd

# class DateInput(forms.DateInput):
#     Input_type="date"

class DateInput(forms.DateInput):
    input_type = 'date'

class LoginForm(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput,label='password')
    password2= forms.CharField(widget=forms.PasswordInput, label='confirm password')
    class Meta:
        model=Login
        fields=('username','password1','password2',)

class userloginform(forms.ModelForm):
    class Meta:
        model=userlogin
        fields=('name','age','address','image')

class eventaddform(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model=eventadd
        fields=('name','date','description','image')
        # fields=('name','date','description')

