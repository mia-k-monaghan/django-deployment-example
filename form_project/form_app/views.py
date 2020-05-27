from django.shortcuts import render
from form_app.forms import SignUp,UserForm,UserInfoForm
from django.contrib.auth.models import User
from .models import UserInfo


# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'form_app/index.html')

def form_view(request):
    form = SignUp()
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form_app/thankyou.html')
    return render(request, 'form_app/signup.html',{'form':form})


def user_signup_view(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        info_form = UserInfoForm(data = request.POST)

        if user_form.is_valid() and info_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            info = info_form.save(commit = False)

            info.user = user

            if 'profile_pic' in request.FILES:
                info.profile_pic = request.FILES['profile_pic']

            info.save()

            registered = True
            return render(request, 'form_app/thankyou.html')

        else:
            print(user_form.errors,info_form.errors)
    else:
        user_form = UserForm()
        info_form = UserInfoForm()

    return render(request, 'form_app/signup.html',
                        {'user_form':user_form,
                        'info_form':info_form,
                        'registered':registered})

def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is not active")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("The username or password does not exist. Please sign up or try again.")
    else:
        return render(request, 'form_app/login.html')

@login_required
def account_view(request):
    user = request.user
    return render(request, 'form_app/my_account.html',{
                                            'user':user,
                                                        })


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
