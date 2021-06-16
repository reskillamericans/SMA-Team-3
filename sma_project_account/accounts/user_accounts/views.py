from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.views import logout_then_login
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.utils import http

from .models import User
from django.contrib.auth.models import auth


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST.get('pwd')
        confirmpwd = request.POST.get('confirmpwd')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        phone = request.POST.get('phone')
        avatar = request.POST.get('avatar')
        occupation = request.POST.get('occupation')
        company = request.POST.get('company')

        if password == confirmpwd:
            try:
                user = User.objects.get(email=email)
                messages.info(request, 'Email is already taken')
                return redirect('user_accounts:register')

            except User.DoesNotExist:
                user = User.objects.create_user(email, username=username, first_name=first_name,
                                                last_name=last_name, password=password, bio=bio, phone=phone,
                                                avatar=avatar, occupation=occupation, company=company)
                user.save()
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('user_accounts:signin')
        elif password == "":
            messages.error(request, 'Password field must be filled')
            return redirect('user_accounts:register')
        else:
            messages.error(request, 'Password must match')
            return redirect('user_accounts:register')

    return render(request, "user_accounts/signup.html")

