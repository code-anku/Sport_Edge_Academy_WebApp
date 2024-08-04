from django.contrib import admin
from .models import feedback, Contact,Event,Coach,Student,Sports_Plan,Sports,Admission


# Register your models here.
admin.site.register(feedback)
admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(Coach)
admin.site.register(Student)
admin.site.register(Sports_Plan)
admin.site.register(Sports)
admin.site.register(Admission)