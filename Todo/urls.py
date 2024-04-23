"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from work.views import Registration,Signin,Add_task,Delete_task,Task_edit,Signout,home,List_task,User_del,Update_user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',Registration.as_view(),name="register"),
    path('log/',Signin.as_view(),name="signin"),
    path('Add/',Add_task.as_view(),name="index"),
    path('delete/<int:pk>',Delete_task.as_view(),name="delete"),
    path('index/update/<int:pk>',Task_edit.as_view(),name='edit'),
    path('signout/',Signout.as_view(),name="logout"),
    path('',home.as_view(),name="Home"),
    path('list/',List_task.as_view(),name="list"),
    path('del_user/<int:pk>',User_del.as_view(),name="del"),
    path('u_user/<int:pk>',Update_user.as_view(),name="update")

   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
