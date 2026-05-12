from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import StudentProfile

# Step 1 Form: Username + Password
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# Step 2 Form: Student Details
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['full_name', 'email', 'profile_photo']