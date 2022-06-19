from multiprocessing import context
from tkinter import NO
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import hospital, blog


def login_user(request, pk):
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
                    hospital_user = hospital.objects.get(
                        user=user, user_type=pk)
                    login(request, user)
                    return redirect('dashboard')
                except:
                    if pk == "DOC":
                        user_type = "DOCTOR"
                    else:
                        user_type = "PATIENT"
                    messages.error(request, 'User is not a '+user_type)
            else:
                messages.error(request, 'Username or Password is incorrect!!')
        except:
            messages.error(request, 'Username does not exist!!')
    context = {'pk': pk, 'title': 'Login'}
    return render(request, 'login.html', context)


def register_user(request, pk):
    context = {'pk': pk, 'title': 'Register'}

    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
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
        try:
            profile_photo = request.FILES['profile_photo']
        # profile_photo = request.POST['profile_photo']
        except:
            profile_photo = ''

        try:
            user = User.objects.get(username=username)
            messages.error(request, 'Username already exist')
        except:
            if password != confirm_password:
                messages.error(request, 'Password does not match...')
            else:
                user = User.objects.create_user(
                    username=username, password=password)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()
                hospital_user = hospital(user=user, user_type=pk, address_line_1=address,
                                         city=city, state=state, pincode=pincode, profile_image=profile_photo)
                hospital_user.save()
                messages.success(request, 'User is created successfully !!!')
                return redirect('login', pk=pk)

    # context={'pk':pk}
    return render(request, "register.html", context)


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    context = {'title': 'home'}
    return render(request, "home.html", context)


def dashboard(request):
    try:
        hospital_user = hospital.objects.get(user=request.user)
        pk = hospital_user.user_type
        return render(request, "dashboard.html", {'hospital_user': hospital_user, 'pk': pk, 'title': 'Profile'})
    except:
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='home')
def all_blog(request):
    user = blog.objects.all()
    hospital_user = hospital.objects.get(user=request.user)
    pk = hospital_user.user_type

    context = {'user': user, 'pk': pk, 'title': 'Blog\'s'}
    return render(request, 'blog.html', context)


@login_required(login_url='home')
def blog_create(request):

    if request.method == 'POST':
        title = request.POST['title']
        summary = request.POST['summary']
        content = request.POST['content']
        category = request.POST['category']
        blog_image = request.FILES['blog_image']

        # user = User.objects.get(user=request.user)
        b = blog.objects.create(
            owner=request.user,
            title=title,
            summary=summary,
            content=content,
            category=category,
            featured_image=blog_image
        )
        return redirect('view-blog')
    hospital_user = hospital.objects.get(user=request.user)
    pk = hospital_user.user_type
    context = {'title': 'Blog', 'pk': pk, 'title': 'Create Blog'}
    return render(request, 'create-blog.html', context)


@login_required(login_url='home')
def view_blog(request):
    user = blog.objects.all()
    username = request.user
    hospital_user = hospital.objects.get(user=request.user)
    pk = hospital_user.user_type

    context = {'user': user, 'pk': pk,
               'username': username, 'title': 'Draft'}
    return render(request, 'view-blog.html', context)


@login_required(login_url='home')
def update_blog(request, pkk):
    update_form = blog.objects.get(id=pkk)
    hospital_user = hospital.objects.get(user=request.user)
    pk = hospital_user.user_type
    if request.method == 'POST':
        title = request.POST['title']
        summary = request.POST['summary']
        content = request.POST['content']
        category = request.POST['category']
        try:
            blog_image = request.FILES['blog_image']
        except:
            blog_image = ''

        update_form.title = title
        update_form.summary = summary
        update_form.content = content
        update_form.category = category
        update_form.featured_image = blog_image
        update_form.save()
        return redirect('dashboard')

    context = {'pk': pk, 'update_form': update_form,
               'pkk': pkk, 'title': 'Update Blog'}
    return render(request, 'update-blog.html', context)


@login_required(login_url='home')
def delete_blog(request, pkk):
    bl = blog.objects.get(id=pkk)
    hospital_user = hospital.objects.get(user=request.user)
    pk = hospital_user.user_type

    if request.method == "POST":
        bl.delete()
        return redirect('view-blog')

    context = {'pk': pk, 'pkk': pkk, 'title': 'Delete Blog', 'sch': bl.title}
    return render(request, 'delete.html', context)
