from twilio.rest import Client
from django.conf import settings
import random


def send_otp_whatsapp(phone_number):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    otp = random.randint(100000, 999999)
    body = f"Your OTP is {otp}"

    message = client.messages.create(
        body=body,
        from_='whatsapp:+8801673850025',
        # This is the sandbox number. Replace it with your Twilio WhatsApp number in production.
        to=f'whatsapp:{phone_number}'
    )

    return otp
