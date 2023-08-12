from django.shortcuts import render

from .forms import LoginForm, RegistrationForm





def index(request):
    
    return render(request, 'webapp/index.html')





