from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from users.forms import UserLoginForm, UserRegisterForm
from django.contrib import messages

def login(request):
  form = UserLoginForm()
  
  if request.method == "POST":
    form = UserLoginForm(request.POST)
    
    if form.is_valid():
      name = form.cleaned_data["name"]
      password = form.cleaned_data["password"]
      
      user = auth.authenticate(
        request,
        username=name,
        password=password,
      )
      
      if user is not None:
        auth.login(request, user)
        messages.success(request, f"Usuário {name} logueado com sucesso")
        return redirect("home")

      messages.error(request, "Usuário ou senha inválidos")
      return redirect("login")
  
  return render(request, "users/login.html", { "form": form })

def register(request):
  form = UserRegisterForm()
  
  if request.method == "POST":
    form = UserRegisterForm(request.POST)
    
    if form.is_valid():
      if form.cleaned_data["password"] != form.cleaned_data["password_confirm"]:
        messages.error(request, "Senhas não conferem")
        return redirect("register")
      
      name = form.cleaned_data["name"]
      email = form.cleaned_data["email"]
      password = form.cleaned_data["password"]
      
      if User.objects.filter(username=name).exists():
        messages.error(request, "Usuário já existe")
        return redirect("register")
      
      user = User.objects.create_user(
        username=name,
        email=email,
        password=password
      )
      user.save()
      messages.success(request, "Usuário criado com sucesso")
      return redirect("login")
  
  return render(request, "users/register.html", { "form": form })

def logout(request):
  messages.success(request, "Usuário deslogado com sucesso")
  auth.logout(request)
  return redirect("login")