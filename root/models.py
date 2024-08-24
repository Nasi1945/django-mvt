from django.db import models
from django.utils import timezone

class Service(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(default='lesson')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)
        
class Events(models.Model):
    image = models.ImageField(upload_to='events',default='event.jpg')
    name = models.CharField(max_length= 100)
    schedule = models.DateTimeField(default=timezone.now)
    content = models.TextField(default='happening')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)


class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email
    
class Contactus(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.email