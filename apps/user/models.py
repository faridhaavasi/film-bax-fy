from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from apps.common.models import BaseModel


from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where phone_number is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not phone_number:
            raise ValueError(_("The phone_number must be set"))
        phone_number = phone_number
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        """
        Create and save a SuperUser with the given phone_number and password.
        """
        extra_fields.setdefault("is_staff", True)

        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))

        return self.create_user(phone_number, password, **extra_fields)





class CustomUser(AbstractBaseUser, BaseModel):
    phone_number = models.CharField(max_length=11, unique=True, db_index=True)
    fullname = models.CharField(null=True, blank=True)
    id_name = models.CharField(unique=True, db_index=True, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.phone_number
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin





