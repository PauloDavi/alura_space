from django.contrib import admin
from gallery.models import Photograph

class ListPhotograph(admin.ModelAdmin):
  list_display = ('id', 'image', 'title', 'category', 'legend', 'published', 'created_at')
  list_display_links = ('id', 'title')
  search_fields = ('title', 'legend')
  list_filter = ('category', 'user')
  list_editable = ('published',)
  readonly_fields = ('created_at',)
  list_per_page = 10

admin.site.register(Photograph, ListPhotograph)
