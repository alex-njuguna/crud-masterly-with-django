from django.shortcuts import render, redirect

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
            # return redirect('')
    
    context = {
        'form':form
    }
    
    return render(request, 'webapp/register.html', context)


def login(request):
    """log in a user"""
    pass
