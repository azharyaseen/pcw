from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name

class Subscribe(models.Model):
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.email

    


