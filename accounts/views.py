from django.shortcuts import render,redirect
from .form import LoginForm
from django.contrib.auth import authenticate,login,logout,password_validation
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(requests):
    if requests.method == 'GET':
        form = LoginForm()
        context = {
            'form':form,
        }
        return render(requests,'accounts/login.html',context=context)
    elif requests.method == 'POST':
        form = LoginForm(requests.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username,password=password)
            if user is not None:
                login(requests,user)
                return redirect('/')
            else:
                messages.add_message(requests,messages.ERROR,'please enter your data in correct way')
                return redirect(requests.path_info)
        else:
            messages.add_message(requests,messages.ERROR,'maybe you are not signup')
            
@login_required()
def logout_view(requests):
    logout(requests)
    return redirect('/')