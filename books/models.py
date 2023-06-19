from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=250, default=" ")
    description = models.TextField()
    dateAdded = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
