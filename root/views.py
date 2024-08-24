from django.shortcuts import render,redirect
from .models import Service , Events
from course.models import Trainers,Courses
from .form import Newsletterform,Contactusform
from django.contrib import messages


def home(requests):
    services = Service.objects.filter(status = True)
    l_trainer = Trainers.objects.filter(status = True)[:3]
    l_course = Courses.objects.filter(status = True)[:3]
    if requests.method == 'GET':
        context = {
            'services' : services,
            'l_trainer' : l_trainer,
            'l_course' : l_course,
        }
        return render(requests,'root/index.html',context=context) 
    elif requests.method == 'POST':
        form = Newsletterform(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('root:home')
        else:
            messages.add_message(requests, messages.ERROR,'please enter a new email')
            return redirect(requests.path_info)
            
            

def contact(requests):
    if requests.method == 'GET':
        return render(requests,'root/contact.html')
    elif requests.method == 'POST':
        form = Contactusform(requests.POST)
        if form.is_valid():
            form.save()
            messages.add_message(requests,messages.SUCCESS,'we recieve your message and will answer you soon')
            return redirect(requests.path_info)
        else:
            messages.add_message(requests,messages.ERROR,'please try again')
            return redirect('root:contact')

def about(requests):
    return render(requests,'root/about.html')

def events(requests):
    event = Events.objects.filter(status = True)
    context = {
        'event': event
    }
    return render(requests,'root/events.html',context=context)






