from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login as login
from django.contrib.auth import logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.utils import timezone

from .forms import LoginForm , RegisterForm , TaskForm
from .models import Task

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            user=request.user
            task=form.save(commit=False)
            task.user=user
            task.save()
            return redirect('todo_list')
    else:
        form = TaskForm()
    return render(request, 'login/add_task.html', {'form': form})
    


@login_required
def todo_list(request):
    digits = Task.objects.all()
    return render(request, 'login/todo_list.html', {'digits' :digits})





def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo_list')
            else:
                return render(request, 'login/login_page.html', {'form': form})
    return render(request, 'login/login_page.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = RegisterForm()
    return render(request, 'login/register_page.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')