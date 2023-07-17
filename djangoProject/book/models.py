from django.db import models


class Book(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(null=False)
    price = models.FloatField(null=False)

    class Meta:
        db_table = 'Books'
