from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

def__str__(self):
    return self.name

