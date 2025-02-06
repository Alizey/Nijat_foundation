from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request , 'nijat/index.html')

def signup(request):
    return render(request , 'nijat/signup.html')

def login(request):
    return render(request , 'nijat/login.html')
