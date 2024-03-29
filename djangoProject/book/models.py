from django.db import models


# <HW> Task 2. Create models
class Book(models.Model):
    # id = models.IntegerField(unique=True, primary_key=True, auto_created=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(null=False)
    price = models.FloatField(null=False)

    class Meta:
        db_table = 'books'
        unique_together = ['title', 'author']   # <HW37> Task 5. Unique title-author combination
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return f"{self.pk}: {self.title} ({self.author}, {self.year})"
