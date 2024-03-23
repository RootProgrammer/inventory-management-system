from django.urls import path
from .views import verify_otp

urlpatterns = [
    # Your other URL patterns
    path('verify-otp/', verify_otp, name='verify_otp_url'),
]
