from django.urls import path
from apps.authentication.views.signup_views import GenerateOTP, VerifyOTP

app_name = 'authentication'

urlpatterns = [
    path('generic_otp', GenerateOTP.as_view(), name='generic_otp'),
    path('verify_otp', VerifyOTP.as_view(), name='verify_otp'),
]