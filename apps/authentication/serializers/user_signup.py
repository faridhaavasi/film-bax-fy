from rest_framework import serializers
from rest_framework.validators import ValidationError
def zero_phone_number_starter(phone_number: str):
    if phone_number[0] != '09':
        raise ValidationError('phone number to be must start ith zero')

class SetPhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_lenght=11, validators=[zero_phone_number_starter,])


class SetOtpCodeSerializer(serializers.Serializer):
    token = serializers.CharField()
    code = serializers.CharField(max_length=4)

class RegisterSerializer(serializers.Serializer):
    token = serializers.CharField()
    password = serializers.CharField()
