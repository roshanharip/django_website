from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.models import User
from datetime import datetime
from home.models import Registration
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        context = {
            'variable1' : "logout",
            'variable2': "Logout"
        }
        return render(request,"index.html",context)
    else:
        context = {
            'variable1' : "login",
            'variable2': "Login"
        }
        return render(request,"index.html",context)
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            # A backend authenticated the credentials
            return render(request,"index.html")
        else:
            return render(request,"login.html")
            # No backend authenticated the credentials
    return render(request,"login.html")
def logoutuser(request):
    logout(request)
    return redirect("/login")   
def createone(request):
    if request.method == "POST":
        date = datetime.today()
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username,email=email,password=password)
        user.first_name = fname
        user.last_name = lname
        user.is_staff = True
        user.date_joined = date
        user.save()
        
    return render(request,'createone.html')
temp = ""
main_otp = 0
def validation(request):
    global temp
    if request.method == "POST":
        email = request.POST.get("email")
        temp = email
        try:
            n= User.objects.get(email=email)
        except:
            n = 0
        print(n) 
        if n:
            print(temp)
            return redirect("otp")
        else:
            return redirect("/validation")

    return render(request,"validation.html")
def otp(request):
    global main_otp,temp
    if request.method == "POST":
        email_otp = request.POST.get('otp')
        if int(email_otp) == main_otp:
            return redirect('/forgotpassword')

    import os, math, random, smtplib
    digits= "0123456789"
    OTP =""
    for i in range(6):
        OTP += digits[math.floor(random.random()*10)]
    otp = OTP + "is your OTP"
    msg = otp
    main_otp = int(OTP)
    print(True,5)
    print(type(temp))
    print(temp)
    print(msg)
    send_mail(
        'OTP FOR FORGOT PASSWORD',
        msg,
        'roshanvarghese7249@gmail.com',
        [temp],
        fail_silently=False
    )
    print(True,6)
    return render(request,"otp.html")
def forgotpassword(request):
    global temp
    if request.method == "POST":
        forgotuser = request.POST.get('newpassword')
        forgotuser2 = request.POST.get('confirmpassword')
        u = User.objects.get(email=temp)
        u.set_password(forgotuser)
        u.save()
        return redirect('login')
    return render(request,"forgotpassword.html")
def about(request):
    return render(request,"about.html")
def attendance(request):
    return render(request,"attendance.html")
def library(request):
    return render(request,"library.html")
def payment(request):
    return render(request,"payment.html")
def notice(request):
    return render(request,"notice.html")
def registration(request): 
    if request.method == "POST":
        fname = request.POST.get("fname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        lname = request.POST.get("lname")
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        city = request.POST.get("city")
        pincode = request.POST.get("pincode")
        state = request.POST.get("state")
        if  request.POST.get("mbc").capitalize() == "Yes":
            mbc = True
        else: 
            mbc = False
        admission = request.POST.get("admission")
        phone = request.POST.get("phone")
        registration = Registration(fname=fname,lname=lname,email=email,password=password,address1=address1,address2=address2,city=city,state=state,pincode=pincode,phone=phone,mbc=mbc,admission=admission,date=datetime.today())
        registration.save()
        messages.success(request,"Successful.......")
    return render(request,"registration.html")
