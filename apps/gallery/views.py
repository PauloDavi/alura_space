from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from apps.gallery.models import Photograph
from apps.gallery.forms import PhotographForm

def index(request):
  if not request.user.is_authenticated:
    messages.error(request, 'Usúario não esta logado')
    return redirect('login')

  photographs = Photograph.objects.order_by("created_at").filter(published=True)
  return render(request, 'gallery/index.html', { 'photographs': photographs })

def img(request, photograph_id):
  photograph = get_object_or_404(Photograph, pk=photograph_id)
  return render(request, 'gallery/img.html', { 'photograph': photograph })

def search(request):
  if not request.user.is_authenticated:
    messages.error(request, 'Usúario não esta logado')
    return redirect('login')
  
  photographs = Photograph.objects.order_by("created_at").filter(published=True)
  
  if "search" in request.GET:
    search = request.GET["search"]
    if search:
      photographs = photographs.filter(title__icontains=search) 
  
  return render(request, 'gallery/search.html', { 'photographs': photographs })

def new_image(request):
  if not request.user.is_authenticated:
    messages.error(request, 'Usúario não esta logado')
    return redirect('login')
  
  if request.method == 'POST':
    form = PhotographForm(request.POST, request.FILES)
    if form.is_valid():
      form.save(user=request.user)
      messages.success(request, 'Imagem adicionada com sucesso')
      return redirect('home')
  else:
    form = PhotographForm()
  
  return render(request, 'gallery/new_img.html', { 'form': form })

def edit_image(request, photograph_id):
  photograph = get_object_or_404(Photograph, pk=photograph_id)
  form = PhotographForm(instance=photograph)
  
  print(request.user.has_perm("change_photograph"))
  print(photograph.user)
  print(request.user)
  
  if not request.user.has_perm("change_photograph") and photograph.user != request.user:
    messages.error(request, 'Você não tem permissão para deletar essa imagem')
    return redirect('home')
  
  if request.method == 'POST':
    form = PhotographForm(request.POST, request.FILES, instance=photograph)
    if form.is_valid():
      form.save(user=request.user)
      messages.success(request, 'Imagem editada com sucesso')
      return redirect('home')
  
  return render(request, 'gallery/edit_img.html', { 'form': form, 'photograph_id': photograph_id })

def delete_image(request, photograph_id):
  photograph = get_object_or_404(Photograph, pk=photograph_id)
  
  if not request.user.has_perm("change_photograph") and photograph.user != request.user:
    messages.error(request, 'Você não tem permissão para deletar essa imagem')
    return redirect('home')
  
  photograph.delete()
  messages.success(request, 'Imagem deletada com sucesso')
  return redirect('home')
