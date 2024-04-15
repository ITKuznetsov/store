from django.shortcuts import render

# Create your views here.

def log(request):
    return render(request, 'users/login.html')


def reg(request):
    return render(request, 'users/registration.html')


def profile(request):
    return render(request, 'users/profile.html')