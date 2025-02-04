from django import forms
from apps.gallery.models import Photograph

class PhotographForm(forms.ModelForm):
  class Meta:
    model = Photograph
    fields = ['title', 'legend', 'category', 'description', 'image']
    
    labels = {
      'title': 'Título',
      'legend': 'Legenda',
      'category': 'Categoria',
      'description': 'Descrição',
      'image': 'Imagem',
    }
    
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'legend': forms.TextInput(attrs={'class': 'form-control'}),
      'category': forms.Select(attrs={'class': 'form-control'}),
      'description': forms.Textarea(attrs={'class': 'form-control'}),
      'image': forms.FileInput(attrs={'class': 'form-control'}),
    }

  def save(self, user, commit=True):
    instance = super().save(commit=False)
    instance.user = user
    if commit:
      instance.save()
    return instance
