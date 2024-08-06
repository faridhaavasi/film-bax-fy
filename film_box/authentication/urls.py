from django.urls import path
from film_box.authentication.views.otp import GenerateOTP, VerifyOTP

urlpatterns = [
    path('generate-otp/', GenerateOTP.as_view(), name='generate_otp'),
    path('verify-otp/', VerifyOTP.as_view(), name='verify_otp'),
]
