from django import forms
from work.models import User,Taskmodel

class Register(forms.ModelForm):

    class Meta:

        model= User
        fields= ['username',"first_name","last_name","email","password"]
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'enter the username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter the first_name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter the last_name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'enter the email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter the password'}),
            
        }
        

class TaskForm(forms.ModelForm):

    class Meta:

        model= Taskmodel
        fields=["task_name","task_description"]
        widgets={
            'task_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter the task'}),
            'task_description':forms.Textarea(attrs={'class':'form-control','column':20,"rows":5,'placeholder':'enter a description'})
        }
        
        

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'enter the username'}))
    password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'enter the password'}))


