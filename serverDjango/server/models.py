from django.db import models

"""from django.contrib.auth.hashers import make_password

class User(models.Model):
    email = models.EmailField(max_length=40, unique=True)
    password = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    birthday = models.DateField()
    guid = models.CharField(max_length=36)
    androidId = models.CharField(max_length=16)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.email"""

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=40, unique=True)  
    password = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    birthday = models.DateField()
    guid = models.CharField(max_length=36)
    androidId = models.CharField(max_length=16)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []