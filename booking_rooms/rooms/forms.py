from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class TypePaymentFilterForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ['daily_payment']
        widgets = {
            'daily_payment': forms.TextInput(attrs={'class': 'form-input'}),
        }


class TypeGuestsFilterForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ['num_guests']
        widgets = {
            'num_guests': forms.TextInput(attrs={'class': 'form-input'}),
        }


class TypePaymentSortingForm(forms.Form):
    order_payment = forms.BooleanField(label='Сортировка по убыванию стоимости', required=False)


class TypeGuestsSortingForm(forms.Form):
    order_guests = forms.BooleanField(label='Сортировка по убыванию количества гостей', required=False)


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class FindRoomForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['start_time', 'end_time']
        widgets = {
            'start_time': forms.DateInput(format='%Y-%m-%d'),
            'end_time': forms.DateInput(format='%Y-%m-%d')
        }


class AddRoomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'].empty_label = 'Комната не выбрана'
        self.fields['user'].empty_label = 'Пользователь не выбран'

    class Meta:
        model = Order
        fields = ['room', 'user', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.DateInput(format='%Y-%m-%d'),
            'end_time': forms.DateInput(format='%Y-%m-%d')
        }


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['room', 'user', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.DateInput(format='%Y-%m-%d'),
            'end_time': forms.DateInput(format='%Y-%m-%d')
        }
