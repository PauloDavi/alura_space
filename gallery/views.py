from django.shortcuts import render

def index(request):
  return render(request, 'gallery/index.html')

def img(request):
  return render(request, 'gallery/img.html')
