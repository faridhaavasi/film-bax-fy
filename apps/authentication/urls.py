from django.urls import path
from apps.authentication.views.signup_views import GenerateOTP, VerifyOTP, RegisterUser

app_name = 'authentication'

urlpatterns = [
    path('generic_otp', GenerateOTP.as_view(), name='generic_otp'),
    path('verify_otp', VerifyOTP.as_view(), name='verify_otp'),
    path('register_user', RegisterUser.as_view(), name='register_user'),
]