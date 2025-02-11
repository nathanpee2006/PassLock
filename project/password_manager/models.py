import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    salt = models.BinaryField(null=True)


class CommonInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    is_favorited = models.BooleanField(default=False) 

    class Meta:
        abstract = True


class Login(CommonInfo):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    website = models.URLField(null=True, blank=True)
    note = models.TextField(blank=True)
    password_nonce = models.CharField(max_length=24, default="")
    password_tag = models.CharField(max_length=24, default="")


class Card(CommonInfo):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cardholder = models.CharField(max_length=100)
    number = models.CharField(max_length=19) 
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=4)
    number_nonce = models.CharField(max_length=24, default="")
    number_tag = models.CharField(max_length=24, default="")
    cvv_nonce = models.CharField(max_length=24, default="")
    cvv_tag = models.CharField(max_length=24, default="")


class PIN(CommonInfo):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=6)
    note = models.TextField(blank=True)
    code_nonce = models.CharField(max_length=24, default="")
    code_tag = models.CharField(max_length=24, default="")


class SecureNote(CommonInfo):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    notes = models.TextField()
    notes_nonce = models.CharField(max_length=24, default="")
    notes_tag = models.CharField(max_length=24, default="")
