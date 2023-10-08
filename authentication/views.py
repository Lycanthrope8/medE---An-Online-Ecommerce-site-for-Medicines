# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from twilio.rest import Client
import random
from django.conf import settings  # Import Django settings module
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from .models import UserProfile  # Import your UserProfile model


def mylogin(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        # Retrieve user profile based on phone number
        user_profile = UserProfile.objects.filter(phone_number=phone_number).first()

        print(user_profile)  # Debug: Print user_profile to check if it's retrieved correctly

        if user_profile is not None and check_password(password, user_profile.password):
            # Password matches, log the user in
            
            user = authenticate(request, username=phone_number, password=password)
            print(user)


            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
        else:
            # User authentication failed, show error message
            messages.error(request, 'Invalid phone number or password. Please try again.')
            return redirect('mylogin')  # Redirect back to the login page if authentication fails

    return render(request, 'login.html')


def verify_otp(request):
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        phone_number = request.session.get('phone_number')

        if user_otp == stored_otp:
            # OTP is correct, create a user profile
            password = request.POST.get('password')

            # Hash the password
            hashed_password = make_password(password)

            # Check if a user profile with the given phone number already exists
            user_profile, created = UserProfile.objects.get_or_create(
                phone_number=phone_number,
                defaults={'password': hashed_password}
            )

            # Clear the OTP data from the session
            del request.session['otp']
            del request.session['phone_number']

            messages.success(request, 'OTP verified successfully!')
            return redirect('mylogin')  # Redirect to the login page
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return redirect('myregister')  # Redirect back to the registration page if OTP is invalid

    # Handle GET requests (if any) here
    return render(request, 'authentication/login.html')


def myregister(request):
    return render(request, 'register.html')

def send_otp(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        otp = str(random.randint(1000, 9999))  # Generate a random 4-digit OTP

        # Send the OTP via Twilio
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=f'Your OTP is: {otp}',
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone_number
        )

        # Store the OTP in session for verification
        request.session['otp'] = otp
        request.session['phone_number'] = phone_number

        return HttpResponse("OTP sent successfully")


