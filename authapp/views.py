from django.http import JsonResponse
from django.views import View
import re
import threading
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
import random

def is_email(input_str):
    try:
        EmailValidator()(input_str)  
        return True
    except ValidationError:
        return False

import random

def send_verification_email(email):
    
    verification_code = random.randint(100000, 999999)

    send_mail(
        subject="Verify your email",
        message=f"Your verification code is: {verification_code}<<<<< by raven ><",
        from_email="test@mailtrap.io", 
        recipient_list=[email],
    )

class AuthView(View):
    def post(self, request):
        input_data = request.POST.get('identifier')
        if is_email(input_data): 
            thread = threading.Thread(target=send_verification_email, args=(input_data,))
            thread.start()
            return JsonResponse({'message': 'Verification email sent.'})
        else:
            code = random.randint(100000, 999999)
            print(f"Verification code for {input_data}: {code}") 
            return JsonResponse({'message': 'Verification code sent to console.'})
