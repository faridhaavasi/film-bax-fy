from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache

from film_box.authentication.serializers.otp import SetPhoneNumberSerializer, VeryfiOtpCodeSerializer
from film_box.authentication.services.otp import set_phone_number_otp_cache
from film_box.authentication.selectors.otp import get_phone_number, get_otp
from film_box.authentication.utils.otp import send_otp_sms


class GenerateOTP(APIView):
    serializer_class = SetPhoneNumberSerializer

    def post(self, request):
        serializer = self.serializer_class
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            set_phone_number_otp_cache(phone_number=phone_number)
            otp = cache.get(key=phone_number)
            send_otp_sms(phone_number=phone_number, otp=otp)
            return Response({'massage': 'OTP sent successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class VerifyOTP(APIView):
    serializer_class = VeryfiOtpCodeSerializer

    def post(self, request):
        serializer = self.serializer_class
        if serializer.is_valid():
            otp = serializer.validated_data['otp']

            phone_number = get_phone_number(otp=otp)
            if phone_number:
                cache_otp = get_otp(phone_number=phone_number)
                if cache_otp == otp:

                    return Response({'massage': 'OTP verified successfully'}, status=status.HTTP_200_OK)
                return Response({'message': 'Otp is not valid'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'local error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
