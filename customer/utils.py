
from django.conf import settings
import africastalking

def send_sms(phone_number, message):
    username = settings.AFRICAS_TALKING_USERNAME
    api_key = settings.AFRICAS_TALKING_API_KEY
    africastalking.initialize(username, api_key)


    sms = africastalking.SMS

    try:
        response = sms.send(message, [phone_number])
        print(response) 
        return response
    except Exception as e:
        print(f"SMS sending failed: {str(e)}")
        return None
