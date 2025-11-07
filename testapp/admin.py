from django.contrib import admin
from.models import Teacher,Course,Student,Grade

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
admin.site.register(Teacher,TeacherAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','code','teacher']
admin.site.register(Course,CourseAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','email']
admin.site.register(Student,StudentAdmin)

class GradeAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'score']
admin.site.register(Grade,GradeAdmin) 

