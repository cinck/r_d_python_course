from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # id = models.IntegerField(unique=True, primary_key=True)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Custom users'
        verbose_name = 'Site User'
        verbose_name_plural = 'Site Users'

    def __str__(self):
        return f"{id}: {self.first_name} {self.last_name} {self.age}"
        pass


# Create your models here.
