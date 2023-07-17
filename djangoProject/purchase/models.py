from django.db import models


class Purchase(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    user = models.ForeignKey('User', related_name='purchases', on_delete=models.CASCADE())
    book = models.ForeignKey('Book', related_name='books', on_delete=models.CASCADE())

    class Meta:
        db_table = 'purchases'
