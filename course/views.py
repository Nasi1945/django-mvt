from django.shortcuts import render
from .models import Courses,Trainers

def courses(requests,**kwargs):
    if requests.GET.get('search') is not None:
        course = Courses.objects.filter(content__contains = requests.GET.get('search'))
    elif kwargs.get('catname'):
        course = Courses.objects.filter(category__name = kwargs.get('catname'))
#    if requests.GET.get('catname'):
#           course = Courses.objects.filter(category__name = requests.GET.get('catname'))
    elif kwargs.get('trainer'):
        course = Courses.objects.filter(trainers__user__username = kwargs.get('trainer'))
    elif kwargs.get('price'):
        course = Courses.objects.filter(fee__lte = float(kwargs.get('price')))
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

def course_details(requests , id):
    cours = Courses.objects.get(id=id)
    context = {
        'cours':cours
    }
    return render(requests,'course/course-details.html',context=context)

