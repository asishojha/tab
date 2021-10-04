from django.urls import path
from .views import index, chk_inc, inc_report, chk_absentees, abs_report, raw_report, subject_relative_report

app_name = 'core'

urlpatterns = [
	path('', index, name='index'),
	path('check-incomplete-students/', chk_inc, name='chk_inc'),
	path('incomplete-students-report/', inc_report, name='inc_report'),
	path('check-absent-students/', chk_absentees, name='chk_absentees'),
	path('absent-students-report/', abs_report, name='abs_report'),
	path('raw-report/', raw_report, name='raw_report'),
	path('relative-subject-list/', subject_relative_report, name='subject_relative_report'),
]