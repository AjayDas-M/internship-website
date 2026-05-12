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