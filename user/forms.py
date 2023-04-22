from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from user.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя', }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Введите почту'}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Введите номер телефона'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'username', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'readonly': True}))
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image')
