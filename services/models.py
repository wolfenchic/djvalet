from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name 
