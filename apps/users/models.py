from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils import timezone


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("role", "Админ")

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must be assigned to is_superuser=True."
            )
        if other_fields.get("is_active") is not True:
            raise ValueError("Superuser must be assigned to is_active=True.")

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_("Введите почту"))

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    ADMIN = "Админ"
    MANAGER = "Менеджер"
    USER_TYPE_CHOICES = (
        (MANAGER, "Менеджер"),
        (ADMIN, "Админ"),
    )
    role = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default=MANAGER)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    new_password = models.CharField(max_length=255, null=True, blank=True)
    new_password2 = models.CharField(max_length=255, null=True, blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return f"{self.role}"


class Assignee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="media")
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.position}"
