from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound,Http404,HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

@login_required
def main_page(request):
	return render(request,"main/main.html")