from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

from apps.classview_user.forms import CustomUserCreationForm


class CustomLogoutView(LogoutView):
    template_name = 'classview_user/logout.html'
    def get(self, request, *args, **kwargs):
        messages.warning(request, f'Logout successfully!')
        return super().get(request, *args, **kwargs)


class CustomLoginView(LoginView):
    settings.LOGIN_REDIRECT_URL = 'classview_success'
    def post(self, request, *args, **kwargs):
        messages.success(request, f'LoggedIn successfully!!!')
        return super().post(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "classview_user/register.html"
    success_url = reverse_lazy('classview_success')
    def form_valid(self, form):
        messages.success(self.request, f"User created successfully with username {form.cleaned_data.get('username')}")
        print(form.cleaned_data)
        return super().form_valid(form)


'''
class UserSignUpCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # print(form_class.cleaned_data) this doesnot work
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(form.cleaned_data)
        obj = form.cleaned_data
        print(obj['username'])
        form.save() ##################  NO NEED TO USE FORM_SAVE AS ITS BASE CLASS SAVES THE FORM BY DEFAULT###############
        return super(UserSignUpCreateView, self).form_valid(form)
'''