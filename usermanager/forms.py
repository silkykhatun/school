from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password


from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationForm(forms.Form):
    username = forms.CharField(
        required=True, widget=forms.TextInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'Username'}))
    email = forms.CharField(
        required=True, widget=forms.EmailInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'Email'}))
    password1 = forms.CharField(
        required=True, widget=forms.PasswordInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'Password'}))
    password2 = forms.CharField(
        required=True, widget=forms.PasswordInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'Password Again'}))
    first_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'First Name'}))
    last_name = forms.CharField(
        required=False, widget=forms.TextInput(attrs={
            'class': 'bn-input', 'placeholder': 'Last Name'}))

    def save(self, *args, **kwargs):
        # super(RegistrationForm, self).save()
        if kwargs['password1'] == kwargs['password2']:
            user = User.objects.create(
                username=kwargs['username'],
                first_name=kwargs['first_name'],
                last_name=kwargs['last_name'],
                email=kwargs['email'],
                password=make_password(kwargs['password1'])
            )
            return user


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True, widget=forms.TextInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'Username'}))
    password = forms.CharField(
        required=True, widget=forms.PasswordInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'Password'}))


class ChangePasswordForm(forms.Form):
    password = forms.CharField(
        required=True, widget=forms.PasswordInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'Current Password'}))
    password1 = forms.CharField(
        required=True, widget=forms.PasswordInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'New Password'}))
    password2 = forms.CharField(
        required=True, widget=forms.PasswordInput(attrs={
            'required': 'true', 'class': 'bn-input',
            'placeholder': 'New Password Again'}))
