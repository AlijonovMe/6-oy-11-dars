from django import forms
from .models import *


class CourseForms(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': "Nomini kiriting",
            'class': "form-control"
        }),
        label=""
    )


class LessonForms(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': "Nomini kiriting",
            'class': "form-control"
        }),
        label=""
    )

    homework = forms.CharField(
        widget=forms.Textarea({
            'placeholder': "Uyga vazifani kiriting",
            'class': "form-control"
        }),
        label=""
    )

    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput({
            'class': 'form-control',
            'type': "datetime-local"
        }),
        input_formats=['%d.%m.%Y %H:%M'],
        label="",
        required=False
    )

    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select({
            'class': "form-select"
        }),
        label=""
    )


class Register(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Foydalanuvchi nomi"
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Elektron pochta manzili"
    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Parol"
    )
    confirm_password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Parolni qayta kiriting"
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Foydalanuvchi nomi"
    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Parol"
    )
