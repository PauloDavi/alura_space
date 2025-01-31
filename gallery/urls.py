from django.urls import path
from gallery.views import index, img, search

urlpatterns = [
  path("", index, name="home"),
  path("img/<int:photograph_id>", img, name="img"),
  path("search/", search, name="search"),
]
