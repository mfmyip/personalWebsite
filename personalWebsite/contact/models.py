from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.email
    