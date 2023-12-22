from django.db import models

# Create your models here.
class Contact(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField()

