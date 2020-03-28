from django.contrib import admin

# Register your models here.
from .models import user,system

admin.site.register(user)
admin.site.register(system)

