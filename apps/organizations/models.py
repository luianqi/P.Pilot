from django.db import models

from apps.users.models import User


class Organization(models.Model):
    name = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    photo = models.ImageField(default='default.png', upload_to="media")
    description = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=150)
    admin = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
