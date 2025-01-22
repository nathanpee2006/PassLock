from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    salt = models.BinaryField(null=True)