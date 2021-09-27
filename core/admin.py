from django.contrib import admin
from .models import Student, CalculatedStudent

admin.site.register((Student, CalculatedStudent))