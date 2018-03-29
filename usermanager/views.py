from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ChangePasswordForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse

from django.contrib.auth import get_user_model
User = get_user_model()


def home(request):
    """Main Homepage."""
    return render(request, 'index.html')


def register(request):
    """Register method."""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save(**data)
            user = authenticate(username=data['username'], password=data['password1'])
            if user:
                login(request, user)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
            messages.error(request, form.errors)

    else:
        form = RegistrationForm()
    ctx = {'form': form}

    return render(request, 'register.html', ctx)


@login_required
def change_password(request):
    """Change password for logged in user."""
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if request.user.check_password(data['password']) and data['password1'] == data['password2']:
                user = User.objects.get(id=request.user.id)
                user.password = make_password(data['password1'])
                user.save()
                messages.error(request, 'Password changed successfully')
                return HttpResponseRedirect(reverse('home'))
            elif not request.user.check_password(data['password']):
                messages.error(request, 'Wrong Password')
                return HttpResponseRedirect(reverse('change_password'))
            else:
                messages.error(request, 'New Password and repeat password does not match.')
                return HttpResponseRedirect(reverse('change_password'))

        else:
            print(form.errors)
            messages.error(request, form.errors)

    else:
        form = ChangePasswordForm()
    ctx = {'form': form}

    return render(request, 'change_password.html', ctx)
