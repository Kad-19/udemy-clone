from django.shortcuts import render,redirect
from .forms import RegisterUser
from django.contrib.auth import login,logout


def sign_up(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
    elif request.method == 'GET':
        form = RegisterUser()

        return render(request, 'registration/signup.html',{'form':form})
    

def log_out(request):
    logout(request)
    return redirect('/login')
