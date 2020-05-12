from django.shortcuts import render
#Django automates register and login forms : )
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
# Create your views here.

def register(response):
    '''

    If response is a post method create a form and if its a valid form then save it
    all built in features of django
    '''
    if response.method == 'POST':
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            #home page when we create one
        return redirect("/home")
    form = UserCreationForm()
    return render(response,"register/register.html",{"form":form})


