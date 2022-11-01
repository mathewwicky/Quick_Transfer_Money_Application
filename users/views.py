from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegistrationForm

def register(request):

    if request.method != 'POST':
        form = UserRegistrationForm()
        
    else:
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request,new_user)
            return redirect('users:login')
    context = {'form':form}
    return render(request , 'registration/register.html', context)

