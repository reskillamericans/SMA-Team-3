from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import logout_then_login
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.db.models.query_utils import Q
import random
from .models import User, Followers, UserSocials
from posts.models import Posts
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
                user_profile = UserSocials.objects.create(user_id=user)
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('authentication:login')
        elif password == "":
            messages.error(request, 'Password field must be filled')
            return redirect('authentication:register')
        else:
            messages.error(request, 'Password must match')
            return redirect('authentication:register')

    return render(request, "authentication/register.html")


@login_required
def update_profile(request):
    user_profile = UserSocials.objects.get(user_id=request.user.id)
    avatar = request.FILES.get('avatar')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        linkedin = request.POST.get('linkedin')
        twitter = request.POST.get('twitter')
        github = request.POST.get('github')
        stackoverflow = request.POST.get('stackoverflow')
        instagram = request.POST.get('instagram')
        facebook = request.POST.get('facebook')

        try:
            user_profile.user_id.username = username
            user_profile.user_id.email = email
            user_profile.user_id.bio = bio
            user_profile.user_id.avatar = avatar
            user_profile.linkedin = linkedin
            user_profile.twitter = twitter
            user_profile.github = github
            user_profile.stackoverflow = stackoverflow
            user_profile.instagram = instagram
            user_profile.facebook = facebook
            user_profile.user_id.save()
            user_profile.save()
            messages.success(request, f'Profile Updated!')
            return redirect('posts:my-profile')

        except UserSocials.DoesNotExist:
            messages.error('User not found!')

    context = {
        'user_profile': user_profile,
        'user_profile.user_id': user_profile.user_id
    }

    return render(request, 'authentication/edit_profile.html', context)


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

@login_required(login_url='/accounts/login/')
def users_list(request):
    users = User.objects.exclude(user=request.user)
    sent_friend_requests = Followers.objects.filter(user_id=request.user)
    my_friends = request.user.friends.all()
    sent_to = []
    friends = []
    for user in my_friends:
        friend = user.friends.all()
        for f in friend:
            if f in friends:
                friend = friend.exclude(user=f.user)
        friends += friend
    for i in my_friends:
        if i in friends:
            friends.remove(i)
    if request.user in friends:
        friends.remove(request.user)
    random_list = random.sample(list(users), min(len(list(users)), 10))
    for r in random_list:
        if r in friends:
            random_list.remove(r)
    friends += random_list
    for i in my_friends:
        if i in friends:
            friends.remove(i)
    for se in sent_friend_requests:
        sent_to.append(se.follower_id)
    context = {
        'users': friends,
        'sent': sent_to
    }
    return render(request, "authentication/users_list.html", context)

@login_required(login_url='/accounts/login/')
def friend_list(request):
    p = request.user
    friends = p.friends.all()
    context={
	'friends': friends
	}
    return render(request, "authentication/friend_list.html", context)

@login_required(login_url='/accounts/login/')
def send_friend_request(request, id):
    user = get_object_or_404(User, id=id)
    friend_request, created = Followers.objects.get_or_create(
            user_id=request.user,
            follower_id=user)
    return HttpResponseRedirect('/accounts/users/{}'.format(user.username))

@login_required(login_url='/accounts/login/')
def cancel_friend_request(request, id):
    user = get_object_or_404(User, id=id)
    print(user)
    friend_request = Followers.objects.filter(user_id=request.user, follower_id=user).first()
    print(friend_request)
    friend_request.delete()
    return HttpResponseRedirect('/accounts/users/{}'.format(user.username))

@login_required(login_url='/accounts/login/')
def accept_friend_request(request, id):
    from_user = get_object_or_404(User, id=id)
    print(from_user)
    friend_request = Followers.objects.filter(user_id=from_user, follower_id=request.user).first()
    print(friend_request)
    user1 = friend_request.user_id
    print(user1)
    user2 = request.user
    print(user2)
    user1.friends.add(user2.id)
    user2.friends.add(user1.id)
    if(Followers.objects.filter(user_id=request.user, follower_id=from_user).first()):
        request_rev = Followers.objects.filter(user_id=request.user, to_user=from_user).first()
        print(request_rev)
        request_rev.delete()
    friend_request.delete()
    return HttpResponseRedirect('/accounts/users/{}'.format(request.user.username))

@login_required(login_url='/accounts/login/')
def delete_friend_request(request, id):
    from_user = get_object_or_404(User, id=id)
    friend_request = Followers.objects.filter(from_user=from_user, to_user=request.user).first()
    friend_request.delete()
    return HttpResponseRedirect('/accounts/users/{}'.format(request.user.username))

@login_required(login_url='/accounts/login/')
def delete_friend(request, id):
    user_profile = request.user
    friend_profile = get_object_or_404(User, id=id)
    user_profile.friends.remove(friend_profile)
    friend_profile.friends.remove(user_profile)
    return HttpResponseRedirect('/accounts/users/{}'.format(friend_profile))

@login_required(login_url='/accounts/login/')
def profile_view(request, username):
    p = User.objects.filter(username=username).first()
    u = p.id
    sent_friend_requests = Followers.objects.filter(user_id=p.id)
    rec_friend_requests = Followers.objects.filter(follower_id=p.id)
    user_posts = Posts.objects.filter(user_id=u)

    friends = p.friends.all()

    # is this user our friend
    button_status = 'none'
    if p not in request.user.friends.all():
        button_status = 'not_friend'

        # if we have sent him a friend request
        if len(Followers.objects.filter(
            user_id=request.user).filter(follower_id=p.id)) == 1:
                button_status = 'friend_request_sent'

        # if we have recieved a friend request
        if len(Followers.objects.filter(
            user_id=p.id).filter(follower_id=request.user)) == 1:
                button_status = 'friend_request_received'

    context = {
        'u': u,
        'button_status': button_status,
        'friends_list': friends,
        'sent_friend_requests': sent_friend_requests,
        'rec_friend_requests': rec_friend_requests,
        'post_count': user_posts.count
    }

    return render(request, "authentication/user_profile.html", context)
