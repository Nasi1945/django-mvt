from django.shortcuts import render, get_object_or_404,redirect
from .models import Courses,Trainers,Comment,Reply
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .form import CommentForm,ReplyForm
from django.contrib import messages

def courses(request,**kwargs):
    if request.GET.get('search') is not None:
        course = Courses.objects.filter(content__contains = request.GET.get('search'))
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
        page_number = request.GET.get('page')
        course = course.get_page(page_number)
    except EmptyPage:
        course = course.get_page(1)
    except PageNotAnInteger:
        course = course.get_page(1)
        
    context = {
        'course' : course,
        'page_number' : page_number,
    }
    return render(request,'course/courses.html',context=context)

def trainers(request):
    trainer = Trainers.objects.filter(status = True)
    context = {
        'trainer' : trainer
    }
    return render(request,'course/trainers.html',context=context)

def course_details(request , id):
    if request.method == 'GET':
        cours = get_object_or_404(Courses,id=id)
        comments = Comment.objects.filter(statue = True,course = cours)
        reply = Reply.objects.filter(statue = True)
        context = {
            'cours':cours,
            'comments' : comments,
            'reply':reply,    
        }
        return render(request,'course/course-details.html',context=context)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,'your comment have been sent')
                return redirect(request.path_info)
            else:
                messages.add_message(request,messages.ERROR,'please try again')
                return redirect(request.path_info)
        else:
            return redirect('accounts:login')

def edit_comment(request,id):
    comment = get_object_or_404(Comment,id = id)
    if request.method == 'GET':
        form = CommentForm(instance=comment)
        context = {
            'form' : form,
        }
        return render(request,'course/edit_comment.html',context=context)
    elif request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.statue = False
            comment.save()
            return redirect('course:course')
        else:
            messages.add_message(request,messages.ERROR,'please try again')
            return redirect(request.path_info)
        
def reply_comment(request,id):
    comments = get_object_or_404(Comment,id = id)
    if request.method == 'GET':
        form = ReplyForm()
        context = {
            'comments':comments,
            'form':form,
        }
        return render(request,'course/reply_comment.html',context=context)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            form = ReplyForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('course:course')
            else:
                messages.add_message(request,messages.ERROR,'please try again')
                return redirect(request.path_info)