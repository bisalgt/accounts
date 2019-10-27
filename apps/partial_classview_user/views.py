from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


class UserRegisterView(View):
    print('Inside usercreateview')

    def get(self, request, *args, **kwargs):
        print('get method callled')
        form = UserCreationForm()
        print('afer instance of form is defined')
        template_name='partial_classview_user/register.html'
        messages.info(request, f'Register page is called to create new user')
        return render(request, template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        print('post method called')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form)
            print(form.cleaned_data)
            print(form.cleaned_data.get('username'))
            form.save()
            messages.success(request, f" Account created successfully for {form.cleaned_data.get('username')}")
            return redirect('partial_success', permanent=True)
        else:
            messages.warning(request, f'Not valid data posted, enter valid data and follow the instructions')
            return render(request, 'partial_classview_user/register.html', {'form':form})