from rest_framework import serializers

class SetPhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)

    def validate_phone_number(self):
        phone_number = self.validated_data['phone_number']
        if phone_number[0] == '0':
            pass
        raise serializers.ValidationError('phone_number is most be start a 0')



class VeryfiOtpCodeSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=4)



