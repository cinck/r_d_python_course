from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    age = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Site users'
        verbose_name = 'Site User'
        verbose_name_plural = 'Site Users'

    def __str__(self):
        return f"{self.pk}: {self.first_name} {self.last_name} '{self.username}'"
        pass


# Create your models here.
