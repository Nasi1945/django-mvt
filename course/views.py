from django.shortcuts import render, get_object_or_404
from .models import Courses,Trainers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def courses(requests,**kwargs):
    if requests.GET.get('search') is not None:
        course = Courses.objects.filter(content__contains = requests.GET.get('search'))
    elif kwargs.get('catname'):
        course = Courses.objects.filter(category__name = kwargs.get('catname'))
    elif kwargs.get('trainer'):
        course = Courses.objects.filter(trainers__user__username = kwargs.get('trainer'))
    elif kwargs.get('price'):
        course = Courses.objects.filter(fee__lte = float(kwargs.get('price')))
    else:
        course = Courses.objects.filter(status = True)
    
    course = Paginator(course, 2)
    try:
        page_number = requests.GET.get('page')
        course = course.get_page(page_number)
    except EmptyPage:
        course = course.get_page(1)
    except PageNotAnInteger:
        course = course.get_page(1)
        
    context = {
        'course' : course,
        'page_number' : page_number,
    }
    return render(requests,'course/courses.html',context=context)

def trainers(requests):
    trainer = Trainers.objects.filter(status = True)
    context = {
        'trainer' : trainer
    }
    return render(requests,'course/trainers.html',context=context)

def course_details(requests , id):
    cours = get_object_or_404(Courses,id=id)
    context = {
        'cours':cours
    }
    return render(requests,'course/course-details.html',context=context)

