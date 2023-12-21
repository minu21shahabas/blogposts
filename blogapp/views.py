from django.shortcuts import render,redirect
import os
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from blogapp.models import bloguser,newpost

# Create your views here.
def home(request):
    return render(request,'homelogin.html')
def signup(request):
    if request.method=="POST":
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['user']
        email=request.POST['mail']
        number=request.POST['mobilenum']
        password=request.POST['pass']
        cpassword=request.POST['cpass']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"This username already exist!!!!")
                return redirect('home')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,                    
                    email=email,
                    username=username,
                    password=password )
                user.save()
                u=User.objects.get(id=user.id)
                teacher=bloguser(mobileno=number,user=u)
                teacher.save()
                return redirect('/')
        else:
            messages.info(request,"password doesnot match...!")
            print("Password is not matching")
            return redirect('home')
        return redirect('home')
    else:
        return render(request,'homelogin.html')
def log(request):
    if request.method=='POST':
        usernme=request.POST['uname']
        password=request.POST['upass']
        print(password)
        user=auth.authenticate(username=usernme,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                # messages.info(request,f'welcome admin')
                return redirect('alogin')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'welcome {usernme}')
                return redirect('ulogin')
        else:
            messages.info(request,'invalid username or password.Try again!!')
            return redirect('home')
    else:
        return render(request,'homelogin.html')
def alogin(request):
    return render(request,'adminlogin.html')
def new_post(request):
    return render(request,'createpost.html')
def addpost(request):
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        recipe=request.POST['recipe']
        if request.FILES.get('pic') is not None:
            bimg=request.FILES.get('pic')
        else:
            bimg="/static/images/default.jpg"
        add=newpost(title=title,desc=desc,recipe=recipe,bimg=bimg)
        add.save()
        return redirect('alogin')
def showsblogs(request):
    show=newpost.objects.all()
    return render(request,'display_blogs.html',{'show':show})
def editblogs(request,id):
    editbl=newpost.objects.get(id=id)
    return render(request,'edit_blogs.html',{'editbl':editbl})
def editpost(request,id):
    if request.method=="POST":
        edit=newpost.objects.get(id=id)
        edit.title=request.POST['title']
        edit.desc=request.POST['desc']
        if len(request.FILES)!=0:
            if len(edit.bimg)>0:
                os.remove(edit.bimg.path)
            edit.bimg=request.FILES.get('pic')
        edit.save()
        return redirect('showsblogs')
    return render(request,'edit_blogs.html')
def deletepost(request,id):
    dele=newpost.objects.get(id=id)
    dele.delete()
    return redirect('showsblogs')
def signout(request):
    return render(request,'homelogin.html')
def ulogin(request):
    ulist=newpost.objects.all()
    return render(request,'userlogin.html',{'ulist':ulist})
def user_signout(request):
    return render(request,'homelogin.html')
def details(request,id):
    det=newpost.objects.get(id=id)
    return render(request,'detailsblog.html',{'detail':det})


