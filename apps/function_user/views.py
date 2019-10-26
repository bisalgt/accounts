from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages


def user_login(request):
    if request.method=='POST':
        print('post method called')
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print('user : ', user)
        if user:
            print('user email :', user.email)
            login(request, user)
            messages.success(request, f'Login successfully -- {user.username}')
            return redirect('success', permanent=True)
        else:
            messages.warning(request, f'You are not authorized to login')
            return redirect('login', permanent=True)
    else:
        print('get method called')
        return render(request, 'function_user/login.html')

@login_required
def user_logout(request):
    print('Inside logout')
    logout(request)
    messages.success(request, f'You are logged out successfully')
    return redirect('success', permanent=True)


def user_register(request):
    template_name = 'function_user/register.html'
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form) # gives the form with all the datas # cleaned data works only inside form.is_valid method
            print(form.cleaned_data) # gives the form datas in dictionary format
            print(form.cleaned_data.get('username')) # to get a particular data
            form.save()
            messages.success(request, f"Account created successfully for {form.cleaned_data.get('username')}")
            return redirect('success', permanent=True)
        else:
            messages.error(request, f"Account failed, ERROR Occured!")
            return render(request, template_name, {'form': form})
    else:
        messages.warning(request, f'User register page')
        form = UserCreationForm()
        return render(request, template_name, {'form': form})