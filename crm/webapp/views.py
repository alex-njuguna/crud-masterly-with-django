from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegistrationForm, CreateRecordForm, UpdateRecordForm
from .models import Record


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

"""
def user_login(request):
    
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
"""

@login_required(login_url='login')
def dashboard(request):
    """display all records"""
    my_records = Record.objects.all()

    context = {
        'records': my_records
    }

    return render(request, 'webapp/dashboard.html', context)


@login_required(login_url='login')
def create_record(request):
    """create a record"""
    form = CreateRecordForm()

    if request.method == 'POST':
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard')
        
    else:
        form = CreateRecordForm()

    context = {
        'form':form
    }
    return render(request, 'webapp/create-record.html', context)


@login_required(login_url='login')
def update_record(request, pk):
    """update a record"""
    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'webapp/update.html', context)


@login_required(login_url='login')
def single_record(request, pk):
    """update a record"""
    all_records = Record.objects.get(id=pk)

    context = {
        'record': all_records
    }

    return render(request, 'webapp/view-record.html', context)


@login_required(login_url='login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    return redirect('dashboard')



