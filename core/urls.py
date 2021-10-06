from django.urls import path
from .views import index, chk_inc, inc_report, chk_absentees, abs_report, raw_report, subject_relative_report, create_calculated_values, apply_absents, apply_awards

app_name = 'core'

urlpatterns = [
	path('', index, name='index'),
	path('check-incomplete-students/', chk_inc, name='chk_inc'),
	path('incomplete-students-report/', inc_report, name='inc_report'),
	path('check-absent-students/', chk_absentees, name='chk_absentees'),
	path('absent-students-report/', abs_report, name='abs_report'),
	path('raw-report/', raw_report, name='raw_report'),
	path('relative-subject-list/', subject_relative_report, name='subject_relative_report'),
	path('create-calculated-values/', create_calculated_values, name='create_calculated_values'),
	path('apply-absentees/', apply_absents, name='apply_absents'),
	path('apply-awards/', apply_awards, name='apply_awards'),
]