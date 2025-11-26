from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(attrs={
            "class": "input-form",
            "placeholder": "Seu usuário"
        })
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "input-form",
            "placeholder": "seuemail@exemplo.com"
        })
    )

    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            "class": "input-form",
            "placeholder": "Crie uma senha"
        })
    )

    password2 = forms.CharField(
        label="Confirmar senha",
        widget=forms.PasswordInput(attrs={
            "class": "input-form",
            "placeholder": "Repita a senha"
        })
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
