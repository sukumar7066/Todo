from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import Register,LoginForm,TaskForm
from work.models import User,Taskmodel
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator


def signin_required(fn):        #Add_task   get(request,**kwargs) post

    def wrapper(request,**kwargs):

        if not request.user.is_authenticated:

            return redirect("signin")
        
        else:

            return fn(request,**kwargs)
    return wrapper


def mylogin(fn):

    def wrapper(request,**kwargs):

        id=kwargs.get("pk")

        obj=Taskmodel.objects.get(id=id)

        if obj.user!= request.user:

            return redirect("signin")
        
        else:

            return fn(request,**kwargs)
        
    return wrapper



class home(View):

    def get(self,request,**kwargs):

        return render(request,"home.html")




class Registration(View):

    def get(self,request,**kwargs):

        form=Register()

        return render(request,"register.html",{"form":form})
    
    def post(self,request,**kwargs):

        form=Register(request.POST)

        if form.is_valid():

            User.objects.create_user(**form.cleaned_data)
            form=Register()
        return render(request,"register.html",{"form":form})

class Update_user(View):

    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        data=User.objects.get(id=id)

        form=Register(instance=data)

        return render(request,"register.html",{"form":form})
    
    def post(self,request,**kwargs):

        id=kwargs.get("pk")
        data=User.objects.get(id=id)
        form=Register(request.POST,instance=data)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")






        

class Signin(View):

    def get(self,request,**kwargs):

        form=LoginForm()

        return render(request,"login.html",{"form":form})
    
    
    def post(self,request,**kwargs):

        form=LoginForm(request.POST)

        if form.is_valid():

            u_name=form.cleaned_data.get("username")

            pwd=form.cleaned_data.get("password")

            user_obj=authenticate(username=u_name,password=pwd)

            if user_obj:
                print("valid credentials")
                login(request,user_obj)
                return redirect("index")   #name="index"
            else:
                form=LoginForm()
                return render(request,"login.html",{"form":form})
@method_decorator(signin_required,name="dispatch")
class Add_task(View):

    def get(self,request,**kwargs):
        
        form=TaskForm()
        data=Taskmodel.objects.filter(user=request.user).order_by('completed')
        return render(request,"index.html",{"form":form,"data":data})

    def post(self,request,**kwargs):

        form=TaskForm(request.POST)
        
        if form.is_valid():

            form.instance.user=request.user

            form.save()
            messages.success(request,"task added successfully")
            

        form=TaskForm()
        data=Taskmodel.objects.filter(user=request.user).order_by('completed')
        return render(request,"index.html",{"form":form,"data":data})
    
class List_task(View):

    def get(self,request,**kwargs):
        qs=Taskmodel.objects.all()
        print(request.GET)
        if "task_name" in request.GET:
            task_name=request.GET.get("task_name")
            qs= qs.filter(task_name__iexact=task_name)
        return render(request,"list.html",{"data":qs}) 
    
    def post(self,request,**kwargs):
        task_name=request.POST.get("box")
        qs=Taskmodel.objects.filter(task_name=task_name)
        return render(request,"list.html",{"data":qs})


@method_decorator(signin_required,name="dispatch")
@method_decorator(mylogin,name='dispatch')
class Delete_task(View):

    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        Taskmodel.objects.get(id=id).delete()

        return redirect("index")
    
class Task_edit(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        obj=Taskmodel.objects.get(id=id)
        
        if obj.completed == False:
            obj.completed = True
            obj.save()
        return redirect("index")
    

    
class Signout(View):

    def get(self,request):

        logout(request)

        return redirect('signin')
    
class User_del(View):

    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        User.objects.get(id=id).delete()

        return redirect("Home")


    

# environment setup
# CRUD
# Course :course_name,course_description
        

    


        

       
        

    



