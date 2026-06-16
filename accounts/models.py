from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "Admin"
        CUSTOMER = "Customer"

    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.NORMAL)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
