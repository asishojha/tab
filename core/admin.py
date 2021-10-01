from django.contrib import admin
from .models import Student, CalculatedStudent

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	search_fields = ['roll_no']

admin.site.register(CalculatedStudent)