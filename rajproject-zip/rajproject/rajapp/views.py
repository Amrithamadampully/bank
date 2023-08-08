from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .  models import *

def customer_form(request):
    if request.method=='POST':
        Username=request.POST['Username']
        dob=request.POST['dob']
        age=request.POST['age']
        gender=request.POST['gender']
        phone=request.POST['phone']
        email=request.POST['email']
        Address=request.POST['Address']
        account=request.POST['account']
        material=request.POST['material']
        parent_selection=request.POST['parent_selection']
        print("application submitted completed successfully ")
        user=Form(Username=Username,dob=dob,age=age,gender=gender,phone=phone,email=email,Address=Address,account=account,material=material,parent_selection=parent_selection)
        user.save()
        return redirect('/')
    return render(request, 'customer_form.html')

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['re-password']
        if password==cpassword:
            user=User.objects.create_user(username=username,password=password)
            user.save()
            return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('customer_form')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')