from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
# login

def login(request):
    if request.method=='POST':
        nameofuser=request.POST['nameofuser']
        password = request.POST['password']
        user = auth.authenticate(nameofuser=nameofuser,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")
    return render(request,"login.html")



# register
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pword = request.POST['password']
        pword1 = request.POST['password1']
        if pword1==pword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('register')
            else:
                user= User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=pword,email=email)
                user.save()
                return redirect('login')

                # print('User created')
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        # return redirect('/')

    return render(request,"register.html")



# logout
def logout(request):
    auth.logout(request)
    return redirect('/')

