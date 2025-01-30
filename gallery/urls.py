from django.urls import path
from gallery.views import index, img

urlpatterns = [
  path("", index, name="home"),
  path("img", img, name="img"),
]
