from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegistrationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
def register(request):

    if request.method != 'POST':
        form = UserRegistrationForm()
        
    else:
        form = UserRegistrationForm(data=request.POST)
        print(form)
        if form.is_valid():
            print(form)
            new_user = form.save()
            login(request,new_user)
            return HttpResponseRedirect(reverse('users:login'))
    context = {'form':form}
    return render(request , 'registration/register.html', context)

