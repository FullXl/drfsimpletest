from django.db import models

# Create your models here.
class Proyect(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  technology = models.CharField(max_length=200)
  rut = models.CharField(max_length=255, default='default_rut')
  members = models.CharField(max_length=255, default='default_rut')
  created_at = models.DateTimeField(auto_now_add=True)







  