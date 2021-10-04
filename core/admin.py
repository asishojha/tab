from django.contrib import admin
from .models import Student, CalculatedStudent

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['roll_no', 'enr_no', 'raw_passed']
	search_fields = ['roll_no']

admin.site.register(CalculatedStudent)