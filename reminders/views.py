from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import TimetableForm
from .models import Automate_text

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






@login_required
def createmsgs(request):
    if request.method == 'GET':
        return render(request, 'reminders/create_msg.html', {'form':TimetableForm()})
    else:
        try:
            form = TimetableForm(request.POST)
            newmsg = form.save(commit=False)
            newmsg.user = request.user
            newmsg.save()
            return redirect('currentmsgs')
        except ValueError:
            return render(request, 'reminders/create_msg.html', {'form':TimetableForm(), 'error':'Bad data passed in. Try again.'})



@login_required
def currentmsgs(request):
    msg = Automate_text.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'reminders/current_msg.html', {'msgs':msg})



@login_required
def completedmsgs(request):
    msg = Automate_text.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'reminders/complete_msg.html', {'msgs':msg})

@login_required
def viewmsgs(request, msg_pk):
    msg = get_object_or_404(Automate_text, pk=msg_pk, user=request.user)
    if request.method == 'GET':
        form = TimetableForm(instance=msg)
        return render(request, 'reminders/view_msgs.html', {'msg':msg, 'form':form})
    else:
        try:
            form = TimetableForm(request.POST, instance=msg)
            form.save()
            return redirect('currentmsgs')
        except ValueError:
            return render(request, 'reminders/view_msgs.html', {'msg':msg, 'form':form, 'error':'Bad info'})

@login_required
def completemsgs(request, msg_pk):
    msg = get_object_or_404(Automate_text, pk=msg_pk, user=request.user)
    if request.method == 'POST':
        msg.datecompleted = timezone.now()
        msg.save()
        return redirect('currentmsgs')

@login_required
def deletemsgs(request, msg_pk):
    msg = get_object_or_404(Automate_text, pk=msg_pk, user=request.user)
    if request.method == 'POST':
        msg.delete()
        return redirect('currentmsgs')
