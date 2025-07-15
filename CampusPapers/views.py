from django.shortcuts import render, get_object_or_404
from .models import University, Faculty, Department, Programme, Year, Semester, AcademicYear, PastPaper

def university_list(request):
    universities = University.objects.all()
    return render(request, 'university_list.html', {'universities': universities})

def faculty_list(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    faculties = Faculty.objects.filter(university=university)
    return render(request, 'faculty_list.html', {'university': university, 'faculties': faculties})

def department_list(request, faculty_id):
    faculty = get_object_or_404(Faculty, pk=faculty_id)
    departments = Department.objects.filter(faculty=faculty)
    return render(request, 'department_list.html', {'faculty': faculty, 'departments': departments})

def programme_list(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    programmes = Programme.objects.filter(department=department)
    return render(request, 'programme_list.html', {'department': department, 'programmes': programmes})

def year_list(request, programme_id):
    programme = get_object_or_404(Programme, pk=programme_id)
    years = Year.objects.filter(programme=programme)
    return render(request, 'year_list.html', {'programme': programme, 'years': years})

def semester_list(request, year_id):
    year = get_object_or_404(Year, pk=year_id)
    semesters = Semester.objects.filter(year=year)
    return render(request, 'semester_list.html', {'year': year, 'semesters': semesters})

def academic_year_list(request, semester_id):
    semester = get_object_or_404(Semester, pk=semester_id)
    academic_years = AcademicYear.objects.filter(semester=semester)
    return render(request, 'academic_year_list.html', {'semester': semester, 'academic_years': academic_years})

def pastpaper_list(request, academic_year_id):
    academic_year = get_object_or_404(AcademicYear, pk=academic_year_id)
    pastpapers = PastPaper.objects.filter(academic_year=academic_year)
    return render(request, 'pastpaper_list.html', {'academic_year': academic_year, 'pastpapers': pastpapers})
