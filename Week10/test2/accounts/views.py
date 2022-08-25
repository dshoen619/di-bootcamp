from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method=="POST":

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email= request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is taken')
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.error(request,'That email is taken')
                return redirect('register')
            
            else:
                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name)
                
                user.save()
                messages.success(request,'You are now registered')
                return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method=="POST":

        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(user=username, passw=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in')
            full_name=User.get_full_name(request)
            context={'user':user,
                     'full_name':full_name,}
            return render(request, 'dashboard.html',context)
        else:
            messages.error(request,'Invalid')
            return redirect('login')

    else:
        return render(request,'accounts/login.html')

def dashboard(request):


    return render(request, 'accounts/dashboard.html')

def logout(request):
    return redirect('index')