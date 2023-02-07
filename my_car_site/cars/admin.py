from django.contrib import admin
from .models import Car

# Register your models here.
# admin.site.register(Car)   delault register

class CarAdmin(admin.ModelAdmin):  # custom register
    fields = ['year', 'brand']
admin.site.register(Car,CarAdmin)