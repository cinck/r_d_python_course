from django.db import models


# <HW> Task 2. Create models
class User(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(null=False)

    class Meta:
        db_table = 'users'

