from django.shortcuts import render
from app_basic_1.forms import UserForm, UserProfileForm

#login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'app_basic_1/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) #hashing the password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'app_basic_1/registration.html', {'user_form':user_form,                  
                                                             'profile_form':profile_form,
                                                             'registered':registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username') # the name in the brackets is from the login.html file
        password = request.POST.get('password') # the name in the brackets is from the login.html file

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index')) # index is taken from the project utls.py
            else:
                return HttpResponse("Account is not active")
        else:
            print("Someone tried to log in and failed!")
            print("Username is {} and password is {}".format(username, password))
            return HttpResponse('Invalid login detailes supplied!')
    else:
        return render(request, 'app_basic_1/login.html')

