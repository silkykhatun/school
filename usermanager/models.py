from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=True)

    def __str__(self, *args, **kwargs):
        return self.username