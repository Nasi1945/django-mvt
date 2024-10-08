from django.urls import path 
from .views import *

app_name = 'course'

urlpatterns = [
    path('',courses , name = 'course'),
    path('category/<str:catname>',courses , name = 'course_category'),
    path('trainer/<str:trainer>',courses , name = 'course_trainer'),
    path('price/<str:price>',courses , name = 'course_price'),
    path('details/<int:id>',course_details , name = 'course_details'),
    path('trainers/',trainers , name = 'trainers'),
    path('comment/<int:id>',edit_comment,name='edit_comment'),
    path('reply/<int:id>',reply_comment,name='reply_comment'),
]
