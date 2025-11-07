from django.shortcuts import render,redirect
from.forms import StudentForm,CourseForm,GradeForm
from.models import Student,Course,Grade


# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request,'testapp/student_list.html',{'students':students})

def student_view(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'testapp/student_view.html', {'student': student})


def student_create(request):
    if request.method == "POST":
        form=StudentForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request,'testapp/insert_student.html',{'form':form})

def student_update(request,pk):
    student=Student.objects.get(pk=pk)
    form=StudentForm(instance=student)
    if request.method == "POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request,'testapp/student_update.html',{'form':form})

 
def student_dlt(request,pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('student_list')

    
def home_redirect(request):
    return redirect('student_list')




def course_list(request):
    courses= Course.objects.all()
    return render(request,'testapp/course_list.html',{'courses':courses})

def course_view(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'testapp/course_view.html', {'course': course})

def course_create(request):
    if request.method == "POST":
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request,'testapp/insert_course.html',{'form':form})

def course_update(request,pk):
    course=Course.objects.get(pk=pk)
    form=CourseForm(instance=course)
    if request.method == "POST":
        form=CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    return render(request,'testapp/update_course.html',{'form':form})


def course_dlt(request,pk):
   course = Course.objects.get(pk=pk)
   course.delete()
   return redirect('course_list')




def grade_list(request):
    grades= Grade.objects.all()
    return render(request,'testapp/grade_list.html',{'grades':grades})

def grade_view(request, pk):
    grade = Grade.objects.get(pk=pk)
    return render(request, 'testapp/grade_view.html', {'grade': grade})

def grade_create(request):
    if request.method == "POST":
        form=GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request,'testapp/insert_grade.html',{'form':form})

def grade_update(request,pk):
    grade=Grade.objects.get(pk=pk)
    form=GradeForm(instance=grade)
    if request.method == "POST":
        form=GradeForm(request.POST,instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    return render(request,'testapp/grade_update.html',{'form':form})


def grade_dlt(request,pk):
  grade = Grade.objects.get(pk=pk)
  grade.delete()
  return redirect('grade_list')








        


    

