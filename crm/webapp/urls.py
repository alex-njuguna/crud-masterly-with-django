from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='webapp/login.html', next_page='dashboard'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('dashboard/', views.dashboard, name='dashboard')
]