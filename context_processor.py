from root.models import Events
from course.models import *
from django.contrib.auth.models import User

def general_objects(requests):
    context = {
        'events' : Events.objects.all().count(),
        'users' : User.objects.all().count(),
        'courses' : Courses.objects.all().count(),
        'category' : Category.objects.all(),
        'trainers' : Trainers.objects.all().count(),
    }
    return context