from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404

import article
from article.models import Article
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordChangeView
from django.urls import reverse_lazy
from .models import *
from .form import *
from django.core.paginator import Paginator
from django.urls import reverse

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    next= request.GET.get('next')
    login_form = Login_Form(request.POST or None)
    if login_form.is_valid():
        cd=login_form.cleaned_data
        user = authenticate(request, username=cd['username'], password=cd['password'])
        if user is not None:
            login(request, user)
            if next:
                return redirect(next)
            else:
                return redirect('accounts:profile_page',request.user.username)
        else:
            login_form.add_error('password','Incorrect username or password')
    context = {'login_form': login_form}
    return render(request, 'templates/user/register/login.html', context)


@login_required()
def log_out(request):
    logout(request)
    return redirect('home:home')


def register(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    register_form = Register_Form()
    if request.method == 'POST':
        register_form = Register_Form(data=request.POST)
        if register_form.is_valid():
            cd = register_form.cleaned_data
            user = User.objects.create_user(username=cd['username'],email=cd['email'],password=cd['password'])
            user.save()
            login(request, user)
            return redirect('accounts:profile_page' , request.user.username)
        else:
            register_form.add_error('password','incorrect Information')
    return render(request, 'templates/user/register/register.html', {'register_form':register_form})


@login_required()
def profile(request,username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    articles = Article.objects.filter(author=user)
    articles_count=articles.count()
    paginator = Paginator(articles.order_by('-update_date'), 6)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {'profile': profile,
               'page_object':page_object,
               'is_owner':request.user == user,
               'articles_count':articles_count}
    return render(request, 'templates/user/profile/profile.html', context)

@login_required()
def edit_profile(request):
    user_profile=get_object_or_404(Profile,user=request.user)
    user=request.user
    form=EditProfileForm(initial={
        'avatar':user_profile.avatar,
        'email':user.email,
        'username':user.username,
        'about_me':user_profile.about_me,
    })
    if request.method == 'POST':
        form=EditProfileForm(request.POST,request.FILES,user=request.user)
        if form.is_valid():

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            avatar = form.cleaned_data['avatar']
            about_me=form.cleaned_data['about_me']

            #user

            user.username = username
            user.email = email
            user.save()

            #user_profile
            if avatar is not None:
                user_profile.avatar = avatar
            user_profile.about_me = about_me
            user_profile.save()
            return redirect('accounts:profile_page',request.user.username )
    context={'form':form,'user':request.user,'profile':user_profile}
    return render (request, 'templates/user/profile/edit_profile.html', context)

class Change_password(PasswordChangeView):

    form_class = ChangepasswordForm

    def get_success_url(self):
        return reverse('accounts:profile_page', kwargs={'username': self.request.user.username})




#forgot the password
class User_password_reset(PasswordResetView):
    template_name = 'password_reset/password_reset.html'
    email_template_name = 'password_reset/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    form_class = CustomPasswordResetForm

class User_password_reset_done(PasswordResetDoneView):
    template_name = 'password_reset/password_reset_done.html'

class User_password_reset_confirm(PasswordResetConfirmView):
    template_name = 'password_reset/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')
    form_class = CustomSetPasswordForm
class User_password_reset_complete(PasswordResetCompleteView):
    template_name = 'password_reset/password_resetcomplete.html'