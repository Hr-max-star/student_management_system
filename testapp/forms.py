
from django import forms
from.models import*


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class GradeForm(forms.ModelForm):
    class Meta:
        model=Grade
        fields='__all__'

