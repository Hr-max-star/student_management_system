from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.code}"

    

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
    
class Grade(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    score=models.PositiveIntegerField()
 
    class Meta:
        unique_together = ('student','course')

    def clean(self):
        if 0 > self.score > 100 :
            raise ValidationError("Score must be between 0 to 100.")
        
    def __str__(self):
        def __str__(self):
            return f"{self.student.name} - {self.course.name} ({self.score})"

