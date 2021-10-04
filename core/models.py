from django.db import models

class RangeDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)

GRADE_DICT = RangeDict({
	range(91, 101): "A1",
	range(81, 91): "A2",
	range(71, 81): "B1",
	range(61, 71): "B2",
	range(51, 61): "C1",
	range(41, 51): "C2",
	range(33, 41): "D",
	range(0, 33): "E"
})

OVGR_DICT = RangeDict({
	range(451, 501): "A1",
	range(401, 451): "A2",
	range(351, 401): "B1",
	range(301, 351): "B2",
	range(251, 301): "C1",
	range(201, 251): "C2",
	range(165, 201): "D",
})

SUBJECT_SHORT_CODE = {
	"01":"ENGB",
	"02":"BNGA",
	"03":"KOK",
	"04":"HINA",
	"05":"MIZA",
	"06":"A",
	"11":"PHYS",
	"12":"CHEM",
	"13":"MATH",
	"14":"BIOS",
	"15":"ECON",
	"16":"CPSC",
	"17":"GEOY",
	"18":"STAT",
	"19":"PSYL",
	"20":"HOME",
	"21":"ACCY",
	"22":"BST",
	"23":"POLS",
	"24":"EDCN",
	"25":"PHIL",
	"26":"HIST",
	"27":"NUTN",
	"28":"MUSE",
	"29":"SOCY",
	"30":"SANS"
}

MAX_THEORY_MARKS = {
	"01":"80",
	"02":"80",
	"03":"80",
	"04":"80",
	"05":"80",
	"06":"80",
	"11":"70",
	"12":"70",
	"13":"80",
	"14":"70",
	"15":"80",
	"16":"70",
	"17":"70",
	"18":"70",
	"19":"70",
	"20":"70",
	"21":"80",
	"22":"80",
	"23":"80",
	"24":"80",
	"25":"80",
	"26":"80",
	"27":"70",
	"28":"45",
	"29":"80",
	"30":"80"
}

PASSING_THEORY_MARKS = {
	"01":"26",
	"02":"26",
	"03":"26",
	"04":"26",
	"05":"26",
	"06":"26",
	"11":"23",
	"12":"23",
	"13":"26",
	"14":"23",
	"15":"26",
	"16":"23",
	"17":"23",
	"18":"23",
	"19":"23",
	"20":"23",
	"21":"26",
	"22":"26",
	"23":"26",
	"24":"26",
	"25":"26",
	"26":"26",
	"27":"23",
	"28":"15",
	"29":"26",
	"30":"26"
}

MAX_PRACT_MARKS = {
	"01":"20",
	"02":"20",
	"03":"20",
	"04":"20",
	"05":"20",
	"06":"20",
	"11":"30",
	"12":"30",
	"13":"20",
	"14":"30",
	"15":"20",
	"16":"30",
	"17":"30",
	"18":"30",
	"19":"30",
	"20":"30",
	"21":"20",
	"22":"20",
	"23":"20",
	"24":"20",
	"25":"20",
	"26":"20",
	"27":"30",
	"28":"55",
	"29":"20",
	"30":"20"
}

PASSING_PRACT_MARKS = {
	"01":"7",
	"02":"7",
	"03":"7",
	"04":"7",
	"05":"7",
	"06":"7",
	"11":"10",
	"12":"10",
	"13":"7",
	"14":"10",
	"15":"7",
	"16":"10",
	"17":"10",
	"18":"10",
	"19":"10",
	"20":"10",
	"21":"7",
	"22":"7",
	"23":"7",
	"24":"7",
	"25":"7",
	"26":"7",
	"27":"10",
	"28":"18",
	"29":"7",
	"30":"7"
}

class Student(models.Model):
	school = models.CharField(max_length=5)
	enr_no = models.CharField(max_length=10)
	enr_yr = models.CharField(max_length=4)
	roll_no = models.CharField(max_length=12)
	stream = models.CharField(max_length=1)
	name = models.CharField(max_length=35)
	sylb = models.CharField(max_length=3)
	sub1 = models.CharField(max_length=2, null=True)
	th1 = models.CharField(max_length=3, null=True)
	pr1 = models.CharField(max_length=2, null=True)
	sub2 = models.CharField(max_length=2)
	th2 = models.CharField(max_length=3, null=True)
	pr2 = models.CharField(max_length=2)
	sub3 = models.CharField(max_length=2)
	th3 = models.CharField(max_length=3, null=True)
	pr3 = models.CharField(max_length=2)
	sub4 = models.CharField(max_length=2)
	th4 = models.CharField(max_length=3, null=True)
	pr4 = models.CharField(max_length=2)
	sub5 = models.CharField(max_length=2)
	th5 = models.CharField(max_length=3, null=True)
	pr5 = models.CharField(max_length=2)
	sub6 = models.CharField(max_length=2, null=True)
	th6 = models.CharField(max_length=3, null=True)
	pr6 = models.CharField(max_length=2, null=True)
	sub7 = models.CharField(max_length=2, null=True)
	th7 = models.CharField(max_length=3, null=True)
	pr7 = models.CharField(max_length=2, null=True)
	exception_code = models.CharField(max_length=1, null=True)
	absent_code = models.CharField(max_length=1, null=True)
	incomplete_code = models.CharField(max_length=1, null=True)
	raw_passed = models.BooleanField(default=False)

	def is_passed_in_th1(self):
		if self.th1 and self.th1 != 'AB' and int(self.th1) >=  int(PASSING_THEORY_MARKS[self.sub1]):
			return True
		else:
			return False

	def is_passed_in_th2(self):
		if self.th2 and self.th2 != 'AB' and int(self.th2) >=  int(PASSING_THEORY_MARKS[self.sub2]):
			return True
		else:
			return False

	def is_passed_in_th3(self):
		if self.th3 and self.th3 != 'AB' and int(self.th3) >=  int(PASSING_THEORY_MARKS[self.sub3]):
			return True
		else:
			return False

	def is_passed_in_th4(self):
		if self.th4 and self.th4 != 'AB' and int(self.th4) >=  int(PASSING_THEORY_MARKS[self.sub4]):
			return True
		else:
			return False

	def is_passed_in_th5(self):
		if self.th5 and self.th5 != 'AB' and int(self.th5) >=  int(PASSING_THEORY_MARKS[self.sub5]):
			return True
		return False

	def is_passed_in_th6(self):
		if self.th6 and self.th6 != 'AB' and int(self.th6) >=  int(PASSING_THEORY_MARKS[self.sub6]):
			return True
		else:
			return False

	def is_passed_in_th7(self):
		if self.th7 and self.th7 != 'AB' and int(self.th7) >=  int(PASSING_THEORY_MARKS[self.sub7]):
			return True
		else:
			return False

	#theory end prac start

	def is_passed_in_pr1(self):
		if self.pr1 and int(self.pr1) >=  int(PASSING_PRACT_MARKS[self.sub1]):
			return True
		else:
			return False

	def is_passed_in_pr2(self):
		if self.pr2 and int(self.pr2) >=  int(PASSING_PRACT_MARKS[self.sub2]):
			return True
		else:
			return False

	def is_passed_in_pr3(self):
		if self.pr3 and int(self.pr3) >=  int(PASSING_PRACT_MARKS[self.sub3]):
			return True
		else:
			return False

	def is_passed_in_pr4(self):
		if self.pr4 and int(self.pr4) >=  int(PASSING_PRACT_MARKS[self.sub4]):
			return True
		else:
			return False

	def is_passed_in_pr5(self):
		if self.pr5 and int(self.pr5) >=  int(PASSING_PRACT_MARKS[self.sub5]):
			return True
		return False

	def is_passed_in_pr6(self):
		if self.pr6 and int(self.pr6) >=  int(PASSING_PRACT_MARKS[self.sub6]):
			return True
		else:
			return False

	def is_passed_in_pr7(self):
		if self.pr7 and int(self.pr7) >=  int(PASSING_PRACT_MARKS[self.sub7]):
			return True
		else:
			return False

	def __str__(self):
		return self.enr_no

class CalculatedStudent(models.Model):
	student = models.OneToOneField(Student, on_delete=models.CASCADE)
	total1 = models.CharField(max_length=3, null=True)
	grade1 = models.CharField(max_length=2, null=True)
	aw1 = models.CharField(max_length=2, null=True)
	total2 = models.CharField(max_length=3, null=True)
	grade2 = models.CharField(max_length=2, null=True)
	aw2 = models.CharField(max_length=2, null=True)
	total3 = models.CharField(max_length=3, null=True)
	grade3 = models.CharField(max_length=2, null=True)
	aw3 = models.CharField(max_length=2, null=True)
	total4 = models.CharField(max_length=3, null=True)
	grade4 = models.CharField(max_length=2, null=True)
	aw4 = models.CharField(max_length=2, null=True)
	total5 = models.CharField(max_length=3, null=True)
	grade5 = models.CharField(max_length=2, null=True)
	aw5 = models.CharField(max_length=2, null=True)
	total6 = models.CharField(max_length=3, null=True)
	grade6 = models.CharField(max_length=2, null=True)
	aw6 = models.CharField(max_length=2, null=True)
	total7 = models.CharField(max_length=3, null=True)
	grade7 = models.CharField(max_length=2, null=True)
	aw7 = models.CharField(max_length=2, null=True)
	aggr = models.CharField(max_length=3, null=True)
	overall_grade = models.CharField(max_length=2, null=True)
	division = models.CharField(max_length=1, null=True)
	comp_ind1 = models.CharField(max_length=1, null=True)
	comp_ind2 = models.CharField(max_length=1, null=True)
	marksheet_no = models.CharField(max_length=6, null=True)
	cert_no = models.CharField(max_length=6, null=True)

	def __str__(self):
		return self.student.enr_no

	def apply_total_base(self):
		if self.student.raw_passed == True:
			if self.student.sub1:
				self.total1=str(int(self.student.th1)+int(self.student.pr1)).zfill(3)
			if self.student.sub2:
				self.total2=str(int(self.student.th2)+int(self.student.pr2)).zfill(3)	
			if self.student.sub3:
				self.total3=str(int(self.student.th3)+int(self.student.pr3)).zfill(3)	
			if self.student.sub4:
				self.total4=str(int(self.student.th4)+int(self.student.pr4)).zfill(3)	
			if self.student.sub5:
				self.total5=str(int(self.student.th5)+int(self.student.pr5)).zfill(3)	
			if self.student.sub6:
				self.total6=str(int(self.student.th6)+int(self.student.pr6)).zfill(3)	# may cause ab error, needs to be handled here!!!!!!
			if self.student.sub7:
				self.total7=str(int(self.student.th7)+int(self.student.pr7)).zfill(3)
			self.save()

	def apply_grades_base(self):
		if self.student.raw_passed == True:
			if self.student.sub1:
				self.grade1 = GRADE_DICT[int(self.total1)]
			if self.student.sub2:
				self.grade2 = GRADE_DICT[int(self.total2)]
			if self.student.sub3:
				self.grade3 = GRADE_DICT[int(self.total3)]
			if self.student.sub4:
				self.grade4 = GRADE_DICT[int(self.total4)]
			if self.student.sub5:
				self.grade5 = GRADE_DICT[int(self.total5)]
			if self.student.sub6:
				self.grade6 = GRADE_DICT[int(self.total6)]
			if self.student.sub7:
				self.grade7 = GRADE_DICT[int(self.total7)]
			self.save()

	def aggregate_base(self):
		if self.student.raw_passed == True:
			if self.student.sub1:
				self.aggr = int(self.total1) + int(self.total2) + int(self.total3) + int(self.total4) + int(self.total5)
			else:
				self.aggr = int(self.total2) + int(self.total3) + int(self.total4) + int(self.total5) + int(self.total6)
			self.save()

	def apply_ovgr_grade(self):
		if self.student.raw_passed == True:
			self.overall_grade = OVGR_DICT[int(self.aggr)]
			self.save()