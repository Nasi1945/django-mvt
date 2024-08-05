from django.shortcuts import render
from .models import Courses,Trainers

def courses(requests):
    if requests.GET.get('catname'):
        course = Courses.objects.filter(category__name = requests.GET.get('catname'))
    else:
        course = Courses.objects.filter(status = True)
    context = {
        'course' : course
    }
    return render(requests,'course/courses.html',context=context)

def trainers(requests):
    trainer = Trainers.objects.filter(status = True)
    context = {
        'trainer' : trainer
    }
    return render(requests,'course/trainers.html',context=context)

def details(requests):
    return render(requests,'course/course-details.html')

