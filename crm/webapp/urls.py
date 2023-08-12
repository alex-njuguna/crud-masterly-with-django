from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name=''),
    path('register/', views.register, name='register'),
]