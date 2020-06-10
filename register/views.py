from django.shortcuts import render
#Django automates register and login forms : )
from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.http import HttpResponse,HttpResponseNotFound,Http404,HttpResponseRedirect
# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from home.views import home_view
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register(response):
    '''

    If response is a post method create a form and if its a valid form then save it
    all built in features of django
    '''
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            #home page when we create one
            success = reverse_lazy('/login/')
        return HttpResponseRedirect('/login/')
    form = RegisterForm()
    return render(response,"register/register.html",{"form":form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("/main")
    else:
        form = AuthenticationForm()
    return render(request,'register/login.html',{'form':form})