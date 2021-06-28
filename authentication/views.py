from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import logout_then_login
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.db.models.query_utils import Q

from .models import User
from django.contrib.auth.models import auth


def register(request):
    if request.method == 'POST':

        username = request.POST.get('username')
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
                return redirect('authentication:register')

            except User.DoesNotExist:
                user = User.objects.create_user(email, username=username, first_name=first_name,
                                                last_name=last_name, password=password, bio=bio, phone=phone,
                                                avatar=avatar, occupation=occupation, company=company)
                user.save()
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('authentication:login')
        elif password == "":
            messages.error(request, 'Password field must be filled')
            return redirect('authentication:register')
        else:
            messages.error(request, 'Password must match')
            return redirect('authentication:register')

    return render(request, "authentication/signup.html")


def login(request):
    if request.user.is_authenticated:
        return redirect('posts:home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = authenticate(email=email, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('posts:home')
        except ValidationError:
            messages.error(request, 'Unable to reach auth server')
            return redirect("authentication:login")

    return render(request, "authentication/login.html")


def forgot_password(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "authentication/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'SMA App',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@smaapp.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect("authentication:login")
            messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="authentication/password/password_reset.html",
                  context={"password_reset_form": password_reset_form})


def home(request):
    return render(request, "posts/home.html")


def logout(request):
    return logout_then_login(request)
