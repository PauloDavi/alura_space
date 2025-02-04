from django.urls import path
from apps.gallery.views import index, img, search, new_image, edit_image, delete_image, filter

urlpatterns = [
  path("", index, name="home"),
  path("img/<int:photograph_id>", img, name="img"),
  path("search/", search, name="search"),
  path("new-image/", new_image, name="new_image"),
  path("edit-image/<int:photograph_id>", edit_image, name="edit_image"),
  path("delete-image/<int:photograph_id>", delete_image, name="delete_image"),
  path("filter/<str:category>", filter, name="filter"),
]
