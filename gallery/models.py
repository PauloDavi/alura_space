from django.db import models
from datetime import datetime

class Photograph(models.Model):
  OPTION_CATEGORY = [
    ("NEBULA", "Nebulosa"),
    ("STAR", "Estrela"),
    ("GALAXY", "Galáxia"),
    ("PLANET", "Planeta"),
  ]
  
  title = models.CharField(max_length=100, null=False, blank=False)
  legend = models.CharField(max_length=150, null=False, blank=False)
  category = models.CharField(max_length=100, choices=OPTION_CATEGORY, default='NEBULA')
  description = models.TextField(null=False, blank=False)
  image = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True)
  published = models.BooleanField(default=False)
  created_at = models.DateTimeField(default=datetime.now, blank=False)

  def __str__(self):
    return self.title
