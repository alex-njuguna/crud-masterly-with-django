from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='webapp/login.html', next_page='dashboard'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    #crud
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-record/', views.create_record, name='create_record'),
    path('view-record/<int:pk>/', views.single_record, name='view-record'),
    path('update-record/<int:pk>/', views.update_record, name='update-record'),
    path('delete-record/<int:pk>/', views.delete_record, name='delete-record'),


]