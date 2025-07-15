from django.db import models

# Create your models here.
from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)

class Faculty(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Programme(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Year(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()

class Semester(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class AcademicYear(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    year_range = models.CharField(max_length=20)

class PastPaper(models.Model):
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='pastpapers/')
