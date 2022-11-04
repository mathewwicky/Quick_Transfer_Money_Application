from datetime import date
import email
from django.utils.translation import gettext_lazy as _
from email.policy import default
from django.utils import timezone
from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255,unique=True, error_messages={
        'unique':("A user with that email already exist.")})
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    nationality = CountryField(blank_label='(select country)')
    is_active = models.BooleanField(('Active'),default=True)
    username = models.CharField(unique=True, max_length=50)
    date_joined = models.DateTimeField(('date joined'),default=timezone.now)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['first_name','last_name','phone_number','email','date_of_birth','username']

    


