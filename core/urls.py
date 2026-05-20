from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('complete-profile/', views.student_profile_create, name='student_profile_create'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('apply/', views.application_form, name='application_form'),
    path('fullstack/', views.fullstack_view, name='fullstack'),
    path('AIML/', views.AIML_view, name='AIML'),
    path('datascience/', views.datascience_view, name='datascience'), # NEW
    path('uiux/', views.uiux_view, name='uiux'),
    path('form/<str:intern_id>/', views.internship_form, name='internship_form'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update-status/<int:selection_id>/', views.update_status, name='update_status'),
    path('view-student/<int:student_id>/', views.view_student, name='view_student'),
    path('send-mails/', views.send_bulk_emails, name='send_bulk_emails'),
    
]