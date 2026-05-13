from django.contrib.auth.models import User
from django.db import models

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    

class Education12(models.Model):
    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)

    subject1 = models.CharField(max_length=100)
    marks1 = models.IntegerField()

    subject2 = models.CharField(max_length=100)
    marks2 = models.IntegerField()

    subject3 = models.CharField(max_length=100)
    marks3 = models.IntegerField()

    subject4 = models.CharField(max_length=100)
    marks4 = models.IntegerField()

    subject5 = models.CharField(max_length=100)
    marks5 = models.IntegerField()

    certificate = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return f"{self.student.username} - 12th"


class InternshipApplication(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=15)
    college_name = models.CharField(max_length=200)
    course_department = models.CharField(max_length=200)
    year_semester = models.CharField(max_length=50)
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/')

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - Application"
    


class Internship(models.Model):
    internship_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.internship_id} - {self.title}"