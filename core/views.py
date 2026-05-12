from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm, StudentProfileForm
from .models import StudentProfile
import random
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Please fill all fields")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)
        messages.success(request, "Account created! Now complete your profile")
        return redirect('student_profile_create')

    return render(request, 'register.html')

def dashboard(request):
    # Force profile completion for all logged in users
    if not StudentProfile.objects.filter(user=request.user).exists():
        messages.warning(request, "You must complete your profile first")
        return redirect('student_profile_create')

    return render(request, 'dashboard.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                profile = StudentProfile.objects.get(user=user)

                if not profile.is_verified:
                    messages.error(request, "Please verify your email first.")
                    return redirect('login')

            except StudentProfile.DoesNotExist:
                messages.error(request, "Please complete your profile first.")
                return redirect('student_profile_create')

            login(request, user)
            return redirect('home')

        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')


def student_profile_create(request):

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        profile_photo = request.FILES.get('profile_photo')

        if not full_name or not email:
            messages.error(request, "Please fill all required fields")
            return redirect('student_profile_create')

        if StudentProfile.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered")
            return redirect('student_profile_create')

        # Generate 6‑digit OTP
        otp = str(random.randint(100000, 999999))

        # Save temporarily (unverified)
        profile = StudentProfile.objects.create(
            user=request.user,
            username=request.user.username,
            full_name=full_name,
            email=email,
            profile_photo=profile_photo,
            otp=otp,
            is_verified=False
        )

        # Send OTP email
        send_mail(
            'Verify Your Email - OTP',
            f'Your OTP is: {otp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        # Store profile ID in session
        request.session['profile_id'] = profile.id

        messages.success(request, "OTP sent to your email. Please verify.")
        return redirect('verify_otp')

    return render(request, 'student_profile.html', {
        'username': request.user.username
    })


def verify_otp(request):
    profile_id = request.session.get('profile_id')

    if not profile_id:
        messages.error(request, "Session expired. Please register again.")
        return redirect('register')

    try:
        profile = StudentProfile.objects.get(id=profile_id)
    except StudentProfile.DoesNotExist:
        messages.error(request, "Profile not found.")
        return redirect('register')

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')

        if entered_otp == profile.otp:
            profile.is_verified = True
            profile.otp = None  # clear OTP
            profile.save()

            # Send confirmation email
            send_mail(
                'Profile Created Successfully',
                f'Hello {profile.full_name}, your student profile has been successfully created and verified.',
                settings.EMAIL_HOST_USER,
                [profile.email],
                fail_silently=False,
            )

            messages.success(request, "Email verified successfully! You can now login.")
            return redirect('login')

        else:
            messages.error(request, "Invalid OTP. Please try again.")

    return render(request, 'verify_otp.html')