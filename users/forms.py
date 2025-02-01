from django import forms

class UserLoginForm(forms.Form):
  name = forms.CharField(
    label='Nome de login',
    required=True,
    max_length=100,
    widget=forms.TextInput(
      attrs={
        "class": "form-control",
        "placeholder": "Ex: João Silva"
      }
    ),
  )
  password = forms.CharField(
    label='Sua senha',
    required=True,
    max_length=100,
    widget=forms.PasswordInput(
      attrs={
        "class": "form-control",
        "placeholder": "Digite sua senha"
      }
    ),
  )

class UserRegisterForm(forms.Form):
  name = forms.CharField(
    label='Nome de cadastro',
    required=True,
    max_length=100,
    widget=forms.TextInput(
      attrs={
        "class": "form-control",
        "placeholder": "Ex: João Silva"
      }
    ),
  )
  email = forms.EmailField(
    label='Email de cadastro',
    required=True,
    max_length=100,
    widget=forms.EmailInput(
      attrs={
        "class": "form-control",
        "placeholder": "Ex: joaosilva@xpto.com"
      }
    ),
  )
  password = forms.CharField(
    label='Sua senha',
    required=True,
    max_length=100,
    widget=forms.PasswordInput(
      attrs={
        "class": "form-control",
        "placeholder": "Digite sua senha"
      }
    ),
  )
  password_confirm = forms.CharField(
    label='Confirme sua senha',
    required=True,
    max_length=100,
    widget=forms.PasswordInput(
      attrs={
        "class": "form-control",
        "placeholder": "Digite sua senha novamente"
      }
    ),
  )
