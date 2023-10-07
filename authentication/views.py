# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from twilio.rest import Client
import random
from django.conf import settings  # Import Django settings module
from .models import UserProfile

# ...
def mylogin(request):
    return render(request, 'login.html')


def verify_otp(request):
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        phone_number = request.session.get('phone_number')

        if user_otp == stored_otp:
            # OTP is correct, create a user profile
            username = request.POST.get('username')
            email = request.POST.get('email')

            # Create and save the user profile
            user_profile, created = UserProfile.objects.get_or_create(
                phone_number=phone_number,
                defaults={'username': username, 'email': email}
            )

            # Clear the OTP data from the session
            del request.session['otp']
            del request.session['phone_number']

            messages.success(request, 'OTP verified successfully!')
            return redirect('home')  # Redirect to a success page
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return redirect('login')  # Redirect back to the login page
    return render(request, 'authentication/login.html')



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

        # return HttpResponse("OTP sent successfully")
    return render(request, 'authentication/login.html')


