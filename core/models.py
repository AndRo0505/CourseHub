from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.code} - {self.title}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'course'], name='unique_student_course')
        ]

    def __str__(self):
        return f"{self.student} -> {self.course}"
