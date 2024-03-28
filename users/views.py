from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'users/home.html', )

def signup(request):
    return render(request, 'users/signup.html', )
