from django.shortcuts import render
#Django automates register and login forms : )
from django.shortcuts import render,redirect
from .forms import RegisterForm
# Create your views here.



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
        return redirect("login/")
    form = RegisterForm()
    return render(response,"register/register.html",{"form":form})


