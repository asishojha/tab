from django.contrib import admin
from .models import Student, CalculatedStudent

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['roll_no', 'enr_no', 'raw_passed']
	search_fields = ['roll_no']

@admin.register(CalculatedStudent)
class CalculatedStudentAdmin(admin.ModelAdmin):
	list_display = ['student', 'total1', 'grade1', 'total2', 'grade2', 'total3', 'grade3', 'total4', 'grade4', 'total5', 'grade5', 'total6', 'grade6', 'total7', 'grade7', 'aggr', 'overall_grade']