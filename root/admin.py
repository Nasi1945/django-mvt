from django.contrib import admin
from .models import Service , Events,Newsletter, Contactus

admin.site.register(Service)
admin.site.register(Events)
admin.site.register(Newsletter)
admin.site.register(Contactus)