from django.db import models


# <HW> Task 2. Create models
class Purchase(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', related_name='purchases', on_delete=models.CASCADE())
    book = models.ForeignKey('Book', related_name='books', on_delete=models.CASCADE())

    class Meta:
        db_table = 'purchases'
        ordering = '-date'          # <HW37> Task 5. Sorting in ascending order
