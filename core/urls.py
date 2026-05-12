from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('complete-profile/', views.student_profile_create, name='student_profile_create'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('logout/', views.logout_view, name='logout')
]