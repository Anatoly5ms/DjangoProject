from django.shortcuts import render
from accounts.models import User
from accounts import forms
from django.urls import reverse_lazy # we use to redirect users after the log in/out
from django.views.generic import CreateView


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


# class LogIn(CreateView):