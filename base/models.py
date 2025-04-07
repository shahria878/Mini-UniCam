from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Result(models.Model):
    student_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student_name} - {self.subject}"
    

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.code} - {self.title}"

class CourseRegistration(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.student_name} ({self.student_id})"

