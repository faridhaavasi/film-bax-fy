from django.core.cache import cache
from random import randint

def set_phone_number_otp_cache(phone_number: str) -> cache:
    otp = randint(1000, 9999)
    return cache.set(key=phone_number, value=otp, timeout=300), cache.set(key=otp, value=phone_number)
