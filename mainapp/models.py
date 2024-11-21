# models.py
from django.db import models

class NavigationItem(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    
    def __str__(self):
        return self.title
        



