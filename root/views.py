from django.shortcuts import render,redirect
from .models import Service , Events
from course.models import Trainers,Courses
from .form import Newsletterform,Contactusform
from django.contrib import messages


def home(request):
    services = Service.objects.filter(status = True)
    l_trainer = Trainers.objects.filter(status = True)[:3]
    l_course = Courses.objects.filter(status = True)[:3]
    if request.method == 'GET':
        context = {
            'services' : services,
            'l_trainer' : l_trainer,
            'l_course' : l_course,
        }
        return render(request,'root/index.html',context=context) 
    elif request.method == 'POST':
        form = Newsletterform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('root:home')
        else:
            messages.add_message(request, messages.ERROR,'please enter a new email')
            return redirect(request.path_info)
            
            

def contact(request):
    if request.method == 'GET':
        return render(request,'root/contact.html')
    elif request.method == 'POST':
        form = Contactusform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'we recieve your message and will answer you soon')
            return redirect(request.path_info)
        else:
            messages.add_message(request,messages.ERROR,'please try again')
            return redirect('root:contact')

def about(request):
    return render(request,'root/about.html')

def events(request):
    event = Events.objects.filter(status = True)
    context = {
        'event': event
    }
    return render(request,'root/events.html',context=context)






