from django.contrib import admin
from .models import StudentProfile, Education12
from .models import InternshipApplication
from .models import Internship

admin.site.register(Internship)
admin.site.register(InternshipApplication)
admin.site.register(StudentProfile)
admin.site.register(Education12)