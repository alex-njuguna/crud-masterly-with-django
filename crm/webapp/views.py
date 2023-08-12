from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegistrationForm


def index(request):
    
    return render(request, 'webapp/index.html')


def register(request):
    """create a new user"""
    form = RegistrationForm()
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {
        'form':form
    }
    
    return render(request, 'webapp/register.html', context)


def user_login(request):
    """log in a user"""
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('dashboard')
    else:
        form = LoginForm()
    
    return render(request, 'webapp/login.html', {'form':form})


@login_required(login_url='login')
def dashboard(request):

    return render(request, 'webapp/dashboard.html')


