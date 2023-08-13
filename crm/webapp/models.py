from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    """table to store records"""
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        ordering = ('-creation_date',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

