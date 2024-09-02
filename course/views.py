from django.shortcuts import render, get_object_or_404,redirect
from .models import Courses,Trainers,Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .form import CommentForm
from django.contrib import messages

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
    if requests.method == 'GET':
        cours = get_object_or_404(Courses,id=id)
        comments = Comment.objects.filter(statue = True,course = cours)
        context = {
            'cours':cours,
            'comments' : comments,    
        }
        return render(requests,'course/course-details.html',context=context)
    elif requests.method == 'POST':
        form = CommentForm(requests.POST)
        if form.is_valid():
            form.save()
            messages.add_message(requests,messages.SUCCESS,'your comment have been sent')
            return redirect(requests.path_info)
        else:
            messages.add_message(requests,messages.ERROR,'please try again')
            return redirect(requests.path_info)

def edit_comment(requests,id):
    comment = get_object_or_404(Comment,id = id)
    if requests.method == 'GET':
        form = CommentForm(instance=comment)
        context = {
            'form' : form,
        }
        return render(requests,'course/edit_comment.html',context=context)
    elif requests.method == 'POST':
        form = CommentForm(requests.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.statue = False
            comment.save()
            return redirect('course:course')
        else:
            messages.add_message(requests,messages.ERROR,'please try again')
            return redirect(requests.path_info)