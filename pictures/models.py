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

class Location(models.Model):
    name = models.CharField(max_length =60)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()