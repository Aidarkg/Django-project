from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.forms import RegisterForm, LoginForm, VerifyForm
from django.contrib.auth import authenticate, login, logout
from user.models import Profile, SMSCode
import random


def register_view(request):
    if request.method == 'GET':
        print(request.user)
        return render(
            request, 
            'user/register.html', 
            {'form': RegisterForm()})
    elif request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            avatar = form.cleaned_data['avatar']
            bio = form.cleaned_data['bio']

            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
                is_active=False
            )

            Profile.objects.create(
                user=user,
                avatar=avatar,
                bio=bio
            )

            code = ''.join([str(random.randint(0, 9)) for _ in range(5)])
            SMSCode.objects.create(
                user=user,
                code=code
            )
            

            return redirect('verify')
        else:
            return render(request, 'user/register.html', {'form': form})
        

def verify_view(request):
    if request.method == "GET":
        return render(request, 'user/verify.html', {'form': VerifyForm()})
    elif request.method == "POST":
        form = VerifyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if SMSCode.objects.filter(code=code).exists():
                sms_code = SMSCode.objects.get(code=code)
                sms_code.user.is_active = True
                sms_code.user.save()
                sms_code.delete()
                return redirect('login')
            else:
                form.add_error(None, 'Неверный код')
            return render(request, 'user/verify.html', {'form': form})




def login_view(request):
    if request.method == 'GET':
        return render(request, 'user/login.html', {'form': LoginForm()})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data) # None or User object
            if user is not None:
                login(request, user)
                return redirect('products_list')
            else:
                form.add_error(None, 'Неправильный логин или пароль')

        return render(request, 'user/login.html', {'form': form})
    

def profile_view(request):
    return render(request, 'user/profile.html')


def logout_view(request):
    logout(request)
    return redirect('login')