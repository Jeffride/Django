from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound,Http404,HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.


def home_view(request):
    template = "home.html"
    context = {}

    #return render(response,"home/home.html")
    return render(request, template,context)