from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from gallery.models import Photograph

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
