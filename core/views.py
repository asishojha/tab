from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, CalculatedStudent

def index(request):
	return render(request, 'core/index.html')

def chk_inc(request):

	# Check Incomplete theory students
	
	students = Student.objects.all()
	for s in students:
		if s.sub1 is not None:
			if s.th1 is None or s.th2 is None or s.th3 is None or s.th4 is None or s.th5 is None:
				s.incomplete_code = '1'
		if s.sub6 is not None:
			if s.th6 is None:
				s.incomplete_code = '1'
		if s.sub7 is not None:
			if s.th7 is None:
				s.incomplete_code = '1'
		s.save()
	return redirect('core:index')

def inc_report(request):

	# Generate report of incomplete students
	
	inc_students = Student.objects.filter(incomplete_code='1')
	context = {
		'inc_students': inc_students
	}
	return render(request, 'core/incomplete_students_report.html', context)

def chk_absentees(request):

	# Check ABSENT Students
	
	students = Student.objects.all()
	for s in students:
		subjects=0
		absent=0
		if s.sub1:
			subjects += 1
			if s.th1 == 'AB':
				absent += 1
		if s.sub2:
			subjects += 1
			if s.th2 == 'AB':
				absent += 1
		if s.sub3:
			subjects += 1
			if s.th3 == 'AB':
				absent += 1
		if s.sub4:
			subjects += 1
			if s.th4 == 'AB':
				absent += 1
		if s.sub5:
			subjects += 1
			if s.th5 == 'AB':
				absent += 1
		if s.sub6:
			subjects += 1
			if s.th6 == 'AB':
				absent += 1
		if s.sub7:
			subjects += 1
			if s.th7 == 'AB':
				absent += 1

		print('subjects', subjects)
		print('absent', absent)

		if subjects == absent:
			s.absent_code = '4'
		
		elif absent > 0 and subjects != absent:
			s.absent_code = '5'
		else:
			s.absent_code = None
		s.save()
	return redirect('core:index')

def abs_report(request):
	# Generate report of absent students
	
	part_abs_students = Student.objects.filter(absent_code='5')
	full_abs_students = Student.objects.filter(absent_code='4')
	context = {
		'part': part_abs_students.count(),
		'full': full_abs_students.count()
	}
	return render(request, 'core/absent_students_report.html', context)

def raw_report(request):
	total_students = Student.objects.all()
	students = Student.objects.exclude(incomplete_code='1').exclude(absent_code='4').exclude(absent_code='5')
	passed_students_count = 0
	passing_studnets_percentage = 0
	for s in students:
		if s.sub1:
			if ((s.sub1 and s.is_passed_in_th1()) and (s.sub2 and s.is_passed_in_th2()) and (s.sub3 and s.is_passed_in_th3()) and (s.sub4 and s.is_passed_in_th4()) and (s.sub5 and s.is_passed_in_th5())) and ((s.sub1 and s.is_passed_in_pr1()) and (s.sub2 and s.is_passed_in_pr2()) and (s.sub3 and s.is_passed_in_pr3()) and (s.sub4 and s.is_passed_in_pr4()) and (s.sub5 and s.is_passed_in_pr5())):
				s.raw_passed = True
				s.save()
				passed_students_count += 1
		else:
			if ((s.sub2 and s.is_passed_in_th2()) and (s.sub3 and s.is_passed_in_th3()) and (s.sub4 and s.is_passed_in_th4()) and (s.sub5 and s.is_passed_in_th5()) and (s.sub6 and s.is_passed_in_th6())) and ((s.sub2 and s.is_passed_in_pr2()) and (s.sub3 and s.is_passed_in_pr3()) and (s.sub4 and s.is_passed_in_pr4()) and (s.sub5 and s.is_passed_in_pr5()) and (s.sub6 and s.is_passed_in_pr6())):
				s.raw_passed = True
				s.save()
				passed_students_count += 1


	total_students_count = total_students.count()

	passing_studnets_percentage = (passed_students_count / total_students_count) * 100 # round off required
	print(passing_studnets_percentage)

	return HttpResponse('Total Students: {}<br>Passed Students: {}<br>Pass Percentage: {}%'.format(total_students_count, passed_students_count, passing_studnets_percentage))


def subject_relative_report(request):
	subject_list = []
	students = Student.objects.all()
	for s in students:
		subject_list.append(s.sub1)
		subject_list.append(s.sub2)
		subject_list.append(s.sub3)
		subject_list.append(s.sub4)
		subject_list.append(s.sub5)
		subject_list.append(s.sub6)
		subject_list.append(s.sub7)

	subject_list = list(set(subject_list))
	subject_list = [i for i in subject_list if i]

	subj_dict = {}

	subj_passed_dict = {}

	for i in subject_list:
		subj_dict[i] = 0


	for sub_code in subject_list:
		for s in students:
			if s.sub1 == sub_code or s.sub2 == sub_code or s.sub3 == sub_code or s.sub4 == sub_code or s.sub5 == sub_code or s.sub6 == sub_code or s.sub7 == sub_code:
				subj_dict[sub_code] += 1

	for k,v in subj_dict.items():
		subj_dict[k] = str(v)			

	for i in subject_list:
		subj_passed_dict[i] = 0

	for sub_code in subject_list:
		for s in students:
			if (s.sub1 == sub_code and s.is_passed_in_th1()):
				subj_passed_dict[sub_code] += 1
			elif s.sub2 == sub_code and s.is_passed_in_th2():
				subj_passed_dict[sub_code] += 1
			elif s.sub3 == sub_code and s.is_passed_in_th3():
				subj_passed_dict[sub_code] += 1
			elif s.sub4 == sub_code and s.is_passed_in_th4():
				subj_passed_dict[sub_code] += 1
			elif s.sub5 == sub_code and s.is_passed_in_th5():
				subj_passed_dict[sub_code] += 1
			elif s.sub6 == sub_code and s.is_passed_in_th6():
				subj_passed_dict[sub_code] += 1
			elif s.sub7 == sub_code and s.is_passed_in_th7():
				subj_passed_dict[sub_code] += 1

	context = {
		'subj_dict': subj_dict,
		'subj_passed_dict': subj_passed_dict,
	}

	return render(request, 'subject-relative-report.html', context)