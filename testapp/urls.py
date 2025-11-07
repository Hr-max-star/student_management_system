from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students/insert/', views.student_create, name='student_create'),
    path('students/<int:pk>/', views.student_view, name='student_view'),
    path('students/update/<int:pk>/', views.student_update, name='student_update'),
    path('students/delete/<int:pk>/', views.student_dlt, name='student_dlt'),

    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_view, name='course_view'),
    path('courses/insert/', views.course_create, name='course_create'),
    path('courses/update/<int:pk>/', views.course_update, name='course_update'),
    path('courses/delete/<int:pk>/', views.course_dlt, name='course_dlt'),

    path('grades/', views.grade_list, name='grade_list'),
    path('grades/insert/', views.grade_create, name='grade_create'),
    path('grades/<int:pk>/', views.grade_view, name='grade_view'),
    path('grades/update/<int:pk>/', views.grade_update, name='grade_update'),
    path('grades/delete/<int:pk>/', views.grade_dlt, name='grade_dlt'),

]
