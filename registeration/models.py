from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.TextField(max_length=100)
    def __str__(self):
        return self.name + '-' + self.email

class system(models.Model):
    ip =  models.GenericIPAddressField()
    def __str__(self):
        return self.ip 

    
    
