from django.core.cache import cache
def get_otp(phone_number: str) -> str:
    otp = cache.get(key=phone_number)
    return str(otp)


def get_phone_number(otp: str) -> str:
    phone_number = cache.get(key=otp)
    return str(phone_number)