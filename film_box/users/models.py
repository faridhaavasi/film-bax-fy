from django.db import models
from film_box.common.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin



class BaseUserManager(BUM):
    def create_user(self, email, phone_number, is_active=True, is_admin=False, password=None):

        if not phone_number:
            raise ValueError("You must enter the phone number")

        user = self.model(email=self.normalize_email(email.lower()), phone_number=phone_number, is_active=is_active, is_admin=is_admin)

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, phone_number, password=None):
        user = self.create_user(
            email=email,
            phone_number=phone_number,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name = "email address",
                              null=True,
                              blank=True,
                              unique=True, db_index=True)
    phone_number = models.CharField(max_length=11,
                                    unique=True,
                                    verbose_name="phone_number",
                                    db_index=True
                                    )


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BaseUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ()

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin







