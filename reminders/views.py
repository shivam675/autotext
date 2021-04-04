from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'reminders/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'reminders/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'reminders/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'reminders/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})





def loginuser(request):
    if request.method == 'GET':
        return render(request, 'reminders/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'reminders/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')



@login_required
def logoutuser(request):
    # if request.method == 'POST':
        # print('something')
    logout(request)
    return redirect('home')
    # else:
        # return HttpResponse('<h1> you need to login first </2>')


