from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == "POST":
        Username = request.POST['username']
        Password = request.POST['password']

        user = authenticate(request, username=Username, password=Password)
    
        if user is not None: 
            login(request, user)
            messages.success(request, "Login successful")
            return render(request, 'home.html')
        else:
            messages.success(request, "Login unsuccessful")
            return redirect(request, 'home')
    else:
        return render(request,'home.html')
    
def logout_user(request):

    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

def scanner(request):

    return render(request, 'scanner.html')


def robotics_lab(request):
    return render(request, 'robotics_lab.html')

def sparkfun(request):
    return render(request, 'sparkfun.html')

def teacherpack(request):
    return render(request, 'teacherpack.html')

def alienware(request):
    return render(request, 'alienware.html')

def spheros(request):
    return render(request, 'spheros.html')

