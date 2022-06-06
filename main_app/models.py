from django.db import models

# Create your models here.
class Watch(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']