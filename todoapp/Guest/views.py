from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import  *


# Create your views here.


def home(request):
    print("HOME PAGE IS GOING TO RENDER")
    return render(request,"home.html")

from django.shortcuts import redirect


@csrf_exempt
def login(request):
    if request.POST:
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        """
        if UserTBL.objects.get(mail=username,password=password):
            ob=UserTBL.objects.get(mail=username,password=password)
            print(ob.Name)
            return render(request,"user/home.html",{"name":ob.Name})
        else:
            dict={"msg":"failed"}
            return render(request,"login.html",dict)
        """


        try:
            ob=UserTBL.objects.get(mail=username,password=password)
            print(ob.Name)
            request.session["email"]=ob.mail
            return redirect('User:home')
        except Exception as e:
            dict={"msg":"failed"}
            return render(request,"login.html",dict)
    return render(request,"login.html")


@csrf_exempt
def register(request):
    if request.POST:
        name=request.POST.get("username")
        mail=request.POST.get("mail")
        password=request.POST.get("password")

        print(name)
        print(mail)
        print(password)     
        try:
            UserTBL.objects.create(Name=name,mail=mail,password=password)
            msg="Registration Done"
            dict={"replay":msg}
            print("Registration Successfull")
            return render(request,"register.html",dict)
        except Exception as e:
            print(e)
            return render(request,"register.html",{"msg":"failed"})

    return render(request,"register.html")







            
        

