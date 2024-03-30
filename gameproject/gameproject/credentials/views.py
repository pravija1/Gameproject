from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect ('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')





def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken already")
                return redirect('register') #this register is the filename  for the register.html
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken already")
                return redirect('register')
            else:
                user= User.objects.create_user(username=username,password=password,first_name=firstName,last_name=lastName,email=email) #create use, adding content to the database
                #auth user- the database field name username = username (this username is variable that hold username)
                user.save() #saving the user
                return redirect('login')
                print("User  created")
        else:
            messages.info(request,"Password Mismatch")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')