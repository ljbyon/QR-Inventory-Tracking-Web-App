from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import SA_Serial_Numbers
from django.shortcuts import get_object_or_404
from datetime import datetime

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
            return render(request, 'home.html')
    else:
        return render(request,'home.html')
    
def logout_user(request):

    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')



def scanner(request):
    if request.method == "POST":
        sa_serial_number = request.POST.get('decodedText')
        print(sa_serial_number)
        sa_serial_object = get_object_or_404(SA_Serial_Numbers, serial_number=sa_serial_number)
        if sa_serial_object.serial_number == sa_serial_number:
            SA_Serial_Numbers.scanned = True
            SA_Serial_Numbers.last_checked = datetime.now().date()
            sa_serial_object.save()
            print("Serial number matched")

    return render(request, 'scanner.html')


def robotics_lab(request):
    return render(request, 'robotics_lab.html')

def sparkfun(request):
    return render(request, 'sparkfun.html')

def teacherpack(request):
    return render(request, 'teacherpack.html')

def alienware(request):
    values = SA_Serial_Numbers.objects.all()
    print(values)
    return render(request, 'alienware.html', {'values' : values})

def spheros(request):
    return render(request, 'spheros.html')

