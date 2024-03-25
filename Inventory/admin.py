from django.contrib import admin
from .models import SA_Serial_Numbers,Alienware,SparkFunKit,teacherpack, Raspberry_Pi
# Register your models here.
admin.site.register(SA_Serial_Numbers)
admin.site.register(Alienware)
admin.site.register(SparkFunKit)
admin.site.register(teacherpack)
admin.site.register(Raspberry_Pi)