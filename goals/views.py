from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm


def index(request):
    form = RegisterForm()
    signin_form = LoginForm
    context = {"regForm": form,
            "loginForm": signin_form
    }
    return render(request, "login.html", context)


def register(request):
    if request.method == "POST":
        bound_form = RegisterForm(request.POST)
        # True or False, based on the validations that were set!
        print(bound_form.is_valid())
        print(bound_form.errors)  # Any errors in this form as a dictionary
        return redirect('/homepage')

def login(request):
    if request.method == "POST":
        bound_form = RegisterForm(request.POST)
        # True or False, based on the validations that were set!
        print(bound_form.is_valid())
        print(bound_form.errors)  # Any errors in this form as a dictionary
        return redirect('/homepage')

def home(request):
        return render(request, "home.html")

def setgoal(request):
    return render(request,"setgoal.html" )

def editgoal(request):
    return render(request,"edit.html" )

def goals(request):
    return render(request,"view.html" )

def editprofile(request):
    return render (request, "profile.html")

def logout(request):
    request.session.flush()
    return redirect('/')