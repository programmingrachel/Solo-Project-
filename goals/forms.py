from django import forms
from django.forms import widgets
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(
    max_length=100, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class GoalForm(forms.Form):
    goal = forms.CharField(widget=forms.Textarea)
    desc_why = forms.CharField(widget=forms.Textarea)
    short_term_goal = forms.CharField(widget=forms.Textarea)
    # start_date = forms.DateInput()
    # target_date = forms.DateInput()

