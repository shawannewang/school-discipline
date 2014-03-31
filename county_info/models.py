from django.db import models

# Create your models here.
class District(models.Model):
	lea_code = models.CharField(max_length=3, verbose_name="Code", primary_key=True)
	lea_name = models.CharField(max_length=150, verbose_name="Name")
	lea_city = models.CharField(max_length=150, verbose_name="City")
	lea_state = models.CharField(max_length=150, verbose_name="State")
	lea_type = models.CharField(max_length=1, verbose_name="Type")
	lea_email = models.CharField(max_length=100, null=True, verbose_name="Email")
	lea_superintendent = models.CharField(max_length=100, null=True, verbose_name="Superintendent")
	lea_website = models.URLField(max_length=250, null=True, verbose_name="Website")

	class Meta(object):
		verbose_name = "School District"
		verbose_name_plural = "School Districts"
		ordering = ('lea_name',)

	def __unicode__(self):
		return U'%s (%s)' %(self.lea_name, self.lea_code)


class Graduation(models.Model):
	district = models.ForeignKey('District')
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	female_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	male_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	native_american_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	asian_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	black_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	hispanic_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	multiracial_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	white_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	freelunch_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	notfreelunch_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	
	class Meta(object):
		verbose_name = "Graduation Rates"
		verbose_name_plural = "Graduation Rates"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s)' %(self.district.lea_name, self.school_year)


class DisciplineRate(models.Model):
	district = models.ForeignKey('District')
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	category = models.CharField(max_length=1)
	school_improvement_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	short_suspensions = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")
	long_suspensions = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")
	expulsions = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")
	crime = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")

	class Meta(object):
		verbose_name = "Discipline Rates"
		verbose_name_plural = "Discipline Rates"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s) - %s' %(self.district.lea_name, self.school_year, self.category)


class Demographics(models.Model):
	district = models.ForeignKey('District')
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	sat_participation = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	sat_average_score = models.IntegerField(max_length=4, null=True)
	expenses_per_pupil = models.DecimalField(max_digits=8, decimal_places=2, null=True)
	percent_native_american = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_asian = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_black = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_hispanic = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_multiracial = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_white = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_pacific_islander = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_male = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_female = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	class Meta(object):
		verbose_name_plural = "Demographics"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s) - %s' %(self.district.lea_name, self.school_year, self.category)


class Attendance(models.Model):
	district = models.ForeignKey('District')
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	total_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	freelunch_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	notfreelunch_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	black_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	hispanic_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	class Meta(object):
		verbose_name = "Attendance Rate"
		verbose_name_plural = "Attendance Rates"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s)' %(self.district.lea_name, self.school_year)


class GradeLevel(models.Model):
	district = models.ForeignKey('District')
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	percent_on_grade_level = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_freelunch_on_grade_level = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_notfreelunch_on_grade_level = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_black_on_grade_level = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_hispanic_on_grade_level = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	class Meta(object):
		verbose_name = "Students At Grade Level"
		verbose_name_plural = "Students At Grade Level"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s)' %(self.district.lea_name, self.school_year)


class SpecialCourses(models.Model):
	district = models.ForeignKey('District')
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	advanced_course_enrollment = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	vocational_course_enrollment = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	class Meta(object):
		verbose_name = "AP/IB & Vocational Enrollment"
		verbose_name_plural = "AP/IB & Vocational Enrollment"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s)' %(self.district.lea_name, self.school_year)

