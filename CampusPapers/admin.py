from django.contrib import admin
from .models import (
    University,
    Faculty,
    Department,
    Programme,
    Year,
    Semester,
    AcademicYear,
    PastPaper
)

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'university')
    search_fields = ['name', 'university__name']
    list_filter = ['university']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'get_university')
    search_fields = ['name', 'faculty__name', 'faculty__university__name']
    list_filter = ['faculty', 'faculty__university']

    def get_university(self, obj):
        return obj.faculty.university.name
    get_university.short_description = 'University'

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'get_faculty', 'get_university')
    search_fields = [
        'name',
        'department__name',
        'department__faculty__name',
        'department__faculty__university__name'
    ]
    list_filter = ['department', 'department__faculty', 'department__faculty__university']

    def get_faculty(self, obj):
        return obj.department.faculty.name
    get_faculty.short_description = 'Faculty'

    def get_university(self, obj):
        return obj.department.faculty.university.name
    get_university.short_description = 'University'

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ('year', 'programme', 'get_department', 'get_faculty', 'get_university')
    search_fields = [
        'year',
        'programme__name',
        'programme__department__name',
        'programme__department__faculty__name',
        'programme__department__faculty__university__name'
    ]
    list_filter = ['programme', 'programme__department', 'programme__department__faculty', 'programme__department__faculty__university']

    def get_department(self, obj):
        return obj.programme.department.name
    get_department.short_description = 'Department'

    def get_faculty(self, obj):
        return obj.programme.department.faculty.name
    get_faculty.short_description = 'Faculty'

    def get_university(self, obj):
        return obj.programme.department.faculty.university.name
    get_university.short_description = 'University'

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'get_programme', 'get_department', 'get_faculty', 'get_university')
    search_fields = [
        'name',
        'year__year',
        'year__programme__name',
        'year__programme__department__name',
        'year__programme__department__faculty__name',
        'year__programme__department__faculty__university__name'
    ]
    list_filter = [
        'year',
        'year__programme',
        'year__programme__department',
        'year__programme__department__faculty',
        'year__programme__department__faculty__university'
    ]

    def get_programme(self, obj):
        return obj.year.programme.name
    get_programme.short_description = 'Programme'

    def get_department(self, obj):
        return obj.year.programme.department.name
    get_department.short_description = 'Department'

    def get_faculty(self, obj):
        return obj.year.programme.department.faculty.name
    get_faculty.short_description = 'Faculty'

    def get_university(self, obj):
        return obj.year.programme.department.faculty.university.name
    get_university.short_description = 'University'

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('year_range', 'semester', 'get_year', 'get_programme', 'get_department', 'get_faculty', 'get_university')
    search_fields = [
        'year_range',
        'semester__name',
        'semester__year__year',
        'semester__year__programme__name',
        'semester__year__programme__department__name',
        'semester__year__programme__department__faculty__name',
        'semester__year__programme__department__faculty__university__name'
    ]
    list_filter = [
        'semester',
        'semester__year',
        'semester__year__programme',
        'semester__year__programme__department',
        'semester__year__programme__department__faculty',
        'semester__year__programme__department__faculty__university'
    ]

    def get_year(self, obj):
        return obj.semester.year.year
    get_year.short_description = 'Year'

    def get_programme(self, obj):
        return obj.semester.year.programme.name
    get_programme.short_description = 'Programme'

    def get_department(self, obj):
        return obj.semester.year.programme.department.name
    get_department.short_description = 'Department'

    def get_faculty(self, obj):
        return obj.semester.year.programme.department.faculty.name
    get_faculty.short_description = 'Faculty'

    def get_university(self, obj):
        return obj.semester.year.programme.department.faculty.university.name
    get_university.short_description = 'University'

@admin.register(PastPaper)
class PastPaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'academic_year', 'get_semester', 'get_year', 'get_programme', 'get_department', 'get_faculty', 'get_university')
    search_fields = [
        'title',
        'academic_year__year_range',
        'academic_year__semester__name',
        'academic_year__semester__year__year',
        'academic_year__semester__year__programme__name',
        'academic_year__semester__year__programme__department__name',
        'academic_year__semester__year__programme__department__faculty__name',
        'academic_year__semester__year__programme__department__faculty__university__name'
    ]
    list_filter = [
        'academic_year',
        'academic_year__semester',
        'academic_year__semester__year',
        'academic_year__semester__year__programme',
        'academic_year__semester__year__programme__department',
        'academic_year__semester__year__programme__department__faculty',
        'academic_year__semester__year__programme__department__faculty__university'
    ]

    def get_semester(self, obj):
        return obj.academic_year.semester.name
    get_semester.short_description = 'Semester'

    def get_year(self, obj):
        return obj.academic_year.semester.year.year
    get_year.short_description = 'Year'

    def get_programme(self, obj):
        return obj.academic_year.semester.year.programme.name
    get_programme.short_description = 'Programme'

    def get_department(self, obj):
        return obj.academic_year.semester.year.programme.department.name
    get_department.short_description = 'Department'

    def get_faculty(self, obj):
        return obj.academic_year.semester.year.programme.department.faculty.name
    get_faculty.short_description = 'Faculty'

    def get_university(self, obj):
        return obj.academic_year.semester.year.programme.department.faculty.university.name
    get_university.short_description = 'University'
