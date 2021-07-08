from django import forms

class Loginform(forms.Form):
    first_Name =forms.CharField(label='First name',max_length=100)
    last_Name =forms.CharField(label='Last name',max_length=100)
    email = forms.EmailField(label='E-mail',max_length=100)