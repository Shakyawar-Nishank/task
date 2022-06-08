from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import hospital
# Create your views here.

def login_user(request,pk):
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                try:
                    hospital_user = hospital.objects.get(user=user, user_type=pk)
                    login(request, user)
                    print(hospital_user,user)
                    return redirect('dashboard')
                    
                except:
                    messages.error(request, 'User is not a '+pk)
            else:
                messages.error(request, 'Username or Password is incorrect!!')
        except:
            messages.error(request, 'Username does not exist!!')
    context = {'pk':pk}
    return render(request, 'login.html', context)
    
def register_user(request,pk):
    context={'pk':pk}
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        profile_photo=request.POST['profile_photo']
        try:
            user = User.objects.get(username=username)
            messages.error(request,'Username already exist')
        except:
            if password!=confirm_password:
                messages.error(request, 'Password does not match...')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()
                hospital_user = hospital(user=user, user_type=pk, address_line_1=address, city=city, state=state, pincode=pincode,profile_image=profile_photo)
                hospital_user.save()
                messages.success(request, 'User is created successfully !!!')
                login(request, user)
                return redirect('dashboard')

    # context={'pk':pk}
    return render(request, "register.html",context)

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, "home.html")

@ login_required(login_url='login')
def dashboard(request):
    hospital_user = hospital.objects.get(user=request.user)
    return render(request,"temp.html", {'hospital_user':hospital_user})

def logout_user(request):
    logout(request)
    return redirect('home')