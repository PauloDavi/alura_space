from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from users.forms import UserLoginForm, UserRegisterForm

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
        return redirect("home")

      return redirect("login")
  
  return render(request, "users/login.html", { "form": form })

def register(request):
  form = UserRegisterForm()
  
  if request.method == "POST":
    form = UserRegisterForm(request.POST)
    
    if form.is_valid():
      if form.cleaned_data["password"] != form.cleaned_data["password_confirm"]:
        return redirect("register")
      
      name = form.cleaned_data["name"]
      email = form.cleaned_data["email"]
      password = form.cleaned_data["password"]
      
      if User.objects.filter(username=name).exists():
        return redirect("register")
      
      user = User.objects.create_user(
        username=name,
        email=email,
        password=password
      )
      user.save()
      
      return redirect("login")
  
  return render(request, "users/register.html", { "form": form })
