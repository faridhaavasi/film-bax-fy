from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.core.cache import cache
from random import randint
from apps.authentication.serializers.user_signup import SetPhoneNumberSerializer, SetOtpCodeSerializer, RegisterSerializer
import uuid
User = get_user_model()

class GenerateOTP(APIView):
    serializer_class = SetPhoneNumberSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            if phone_number:
                token = str(uuid.uuid4())
                otp = randint(1000,9999)
                cache.set(f"{token}_phone_number", phone_number, timeout=300)
                cache.set(f"{token}_otp", otp, timeout=300)

                # TODO : writhe send sms function and send token function
                print('token:', token, 'otp:', otp)
                return Response({'message': 'otp created'}, status=status.HTTP_201_CREATED)
            return Response({'message': 'phone_number ins nor none'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTP(APIView):
    serializer_class = SetOtpCodeSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            code = serializer.validated_data['code']
            if token and code:
                stored_otp = cache.get(f"{token}_otp")
                if stored_otp is None:
                    return Response({'message': 'OTP expired or invalid'}, status=status.HTTP_400_BAD_REQUEST)
                if str(stored_otp) == str(code):
                    return Response(({'message': 'OTP verified successfully. Proceed to registration.', 'token': token}))
                return Response({'error': 'invalid otp'}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RegisterUser(APIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            password = serializer.validated_data['password']
            phone_number = cache.get(f"{token}_phone_number")
            if not phone_number:
                return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(phone_number=phone_number).exists():
                return Response({'error': 'User already taken'}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create_user(phone_number=phone_number, password=password)
            user.save()
            cache.delete(f"{token}_phone_number")
            return Response({'message': 'User created successfully', 'phone_number': phone_number})









