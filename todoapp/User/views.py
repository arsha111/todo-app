from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import *
from Guest.models import *



@csrf_exempt
def AddTodo(request):
    if request.POST:
        todo=request.POST.get("todo")
        desc=request.POST.get("desc")
        user=request.session["email"]
        ob=UserTBL.objects.get(mail=user)
        print(todo,desc,user)
        try:
            Todolist.objects.create(user=ob,Todo_name=todo,description=desc)
            return redirect('User:home')
        except Exception as e:
            print(e)
            return render(request,"user/addtodo.html",{"data":"failed"})
    return render(request,"user/addtodo.html")

@csrf_exempt
def home(request):
    mail=request.session["email"]
    ob1=UserTBL.objects.get(mail=mail)
    ob=Todolist.objects.filter(user=ob1)

    return render(request,"user/home.html",{"name":ob1.Name,"data":ob})

def delete(request,id):
    print(id)
    ob=Todolist.objects.get(id=id)
    ob.delete()
    return redirect('User:home')

def edit(request,id):
    ob=Todolist.objects.get(id=id)
    return render(request,"user/edit.html",{"data":ob})
@csrf_exempt
def edit1(request):
    id=request.POST.get("id") 
    todo=request.POST.get("todo") 
    desc=request.POST.get("desc")
    ob=Todolist.objects.get(id=id)
    ob.Todo_name=todo
    ob.description=desc
    ob.save()
    return redirect('User:home')
