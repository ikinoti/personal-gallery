from django.db import models

# Create your models here.
# Create your models here.
class Editor(models.Model):
  name = models.CharField(max_length=30)
  email = models.EmailField()
  phone_number = models.CharField(max_length=10, blank=True)

  def __str__(self):
      return self.name

  class Meta:
    ordering = ['name']