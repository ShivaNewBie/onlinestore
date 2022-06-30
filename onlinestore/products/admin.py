from django.contrib import admin

# Register your models here.

from .models import Manufacture,Product

admin.site.register(Manufacture)
admin.site.register(Product)