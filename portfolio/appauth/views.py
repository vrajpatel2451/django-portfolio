import re
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

# Create your views here.
def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request,username=username,password=password)

        if user is not None:
            print('logged in')
            login(request=request,user=user)
            return redirect('/')
        else:
            form = AuthenticationForm()
            return render(request=request,template_name='auth.html',context={'form':form,'pageName':'Login'})
        
    
    form = AuthenticationForm()
    return render(request=request,template_name='auth.html',context={'form':form,'pageName':'Login'})

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request=request,username=username,password=password)
            # if user is not None:
            # print('logged in')
            login(request=request,user=user)
            return redirect('/')
        else:
            form = UserCreationForm()
            return render(request=request,template_name='auth.html',context={'form':form,'pageName':'Register'})
        
    
    form = UserCreationForm()
    return render(request=request,template_name='auth.html',context={'form':form,'pageName':'Register'})

def signout(request):
    logout(request=request)
    return redirect('/auth/login')