# from django.http import JsonResponse
# from django.views import View
# import re
# import threading
# from django.core.mail import send_mail
# from django.core.exceptions import ValidationError
# from django.core.validators import EmailValidator
# import random

# def is_email(input_str):
#     try:
#         EmailValidator()(input_str)  
#         return True
#     except ValidationError:
#         return False

# import random

# def send_verification_email(email):
    
#     verification_code = random.randint(100000, 999999)

#     send_mail(
#         subject="Verify your email",
#         message=f"Your verification code is: {verification_code}<<<<< by raven ><",
#         from_email="test@mailtrap.io", 
#         recipient_list=[email],
#     )

# class AuthView(View):
#     def post(self, request):
#         input_data = request.POST.get('identifier')
#         if is_email(input_data): 
#             thread = threading.Thread(target=send_verification_email, args=(input_data,))
#             thread.start()
#             return JsonResponse({'message': 'Verification email sent.'})
#         else:
#             code = random.randint(100000, 999999)
#             print(f"Verification code for {input_data}: {code}") 
#             return JsonResponse({'message': 'Verification code sent to console.'})


# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from .models import Card, Order, Like
# from .serializers import CardSerializer, OrderSerializer, LikeSerializer

# class CardViewSet(viewsets.ModelViewSet):
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     @action(detail=True, methods=['post'])
#     def qabul_qilish(self, request, pk=None):
#         order = self.get_object()
#         order.status = 'accepted'
#         order.save()
#         return Response({'status': 'Order accepted'})

# class LikeViewSet(viewsets.ModelViewSet):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer


from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
