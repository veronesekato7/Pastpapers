from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('universities/', views.university_list, name='university_list'),
    path('faculties/<int:university_id>/', views.faculty_list, name='faculty_list'),
    path('departments/<int:faculty_id>/', views.department_list, name='department_list'),
    path('programmes/<int:department_id>/', views.programme_list, name='programme_list'),
    path('years/<int:programme_id>/', views.year_list, name='year_list'),
    path('semesters/<int:year_id>/', views.semester_list, name='semester_list'),
    path('academicyears/<int:semester_id>/', views.academic_year_list, name='academic_year_list'),
    path('pastpapers/<int:academic_year_id>/', views.pastpaper_list, name='pastpaper_list'),
]
