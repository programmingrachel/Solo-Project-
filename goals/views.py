from django.shortcuts import render
from .forms import Loginform

def index(request):
    form = Loginform
    return render(request, 'index.html',{'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')