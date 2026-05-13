from django.contrib import admin
from .models import StudentProfile
from .models import InternshipApplication
from .models import Internship
from .models import InternshipSelection

admin.site.register(InternshipSelection)
admin.site.register(Internship)
admin.site.register(InternshipApplication)
admin.site.register(StudentProfile)
