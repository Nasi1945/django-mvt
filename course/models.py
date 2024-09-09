from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
        
class Skills(models.Model):
    name = models.CharField(max_length= 100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
        
class Trainers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='trainers',default= 'unknown.jpg')
    skills = models.ManyToManyField(Skills)
    content = models.TextField('good teacher')
    twitter = models.CharField(max_length= 120,blank=True,null=True)
    instagram = models.CharField(max_length= 120,blank=True,null=True)
    facebook = models.CharField(max_length= 120,blank=True,null=True)
    linkedin = models.CharField(max_length= 120,blank=True,null=True)
    status = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.user.username
    
    class Mata:
        ordering = ('created_at',)
        
class Courses(models.Model):
    name = models.CharField(max_length= 100)
    trainers = models.ForeignKey(Trainers,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    fee = models.FloatField(default= 100)
    likes = models.IntegerField()
    capacity = models.IntegerField(default= 20)
    image = models.ImageField(upload_to='courses',default='course.jpg')
    schedule = models.DateTimeField(default= timezone.now)
    content = models.TextField(default='good lesson')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
        
class Comment(models.Model):
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    statue = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name.username
    
class Reply(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    statue = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name.username
    