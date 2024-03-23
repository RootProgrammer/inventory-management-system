from .utils import send_otp_whatsapp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


def register_user(request):
    if request.method == 'POST':
        # Extract phone_number from request
        phone_number = request.POST.get('phone_number')
        # Generate and send OTP
        otp = send_otp_whatsapp(phone_number)
        # Store the OTP in session or database for verification
        request.session['otp'] = otp
        # Proceed with your registration logic


def verify_otp(request):
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        if 'otp' in request.session:
            correct_otp = request.session['otp']
            if user_otp == correct_otp:
                # OTP is correct
                del request.session['otp']  # Clear OTP from session after verification
                # Proceed with further actions, e.g., activating the user account
                messages.success(request, 'OTP verified successfully.')
                return redirect('success_url')  # Redirect to a success page or further action
            else:
                # OTP is incorrect
                messages.error(request, 'Invalid OTP. Please try again.')
                return redirect('verify_otp_url')  # Redirect back to OTP verification page
        else:
            # No OTP in session
            messages.error(request, 'OTP has expired or is invalid. Please start over.')
            return redirect('signup_url')  # Redirect to signup or resend OTP page
    else:
        return render(request, 'accounts/verify_otp.html')  # Render OTP verification page
