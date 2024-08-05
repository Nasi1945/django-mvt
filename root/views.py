from django.shortcuts import render
from .models import Service , Events
from course.models import Trainers,Courses


def home(requests):
    services = Service.objects.filter(status = True)
    l_trainer = Trainers.objects.filter(status = True)[:3]
    l_course = Courses.objects.filter(status = True)[:3]
    context = {
        'services' : services,
        'l_trainer' : l_trainer,
        'l_course' : l_course,
    }
    return render(requests,'root/index.html',context=context) 

def contact(requests):
    return render(requests,'root/contact.html')

def about(requests):
    return render(requests,'root/about.html')

def events(requests):
    event = Events.objects.filter(status = True)
    context = {
        'event': event
    }
    return render(requests,'root/events.html',context=context)






