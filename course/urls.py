from django.urls import path 
from .views import *

app_name = 'course'

urlpatterns = [
    path('',courses , name = 'course'),
    path('trainers/',trainers , name = 'trainers'),
    path('details',details , name= 'details'),
]
