from django.db import models
from users.models import User
from book.models import Book


# <HW> Task 2. Create models
class Purchase(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, auto_created=True)
    date = models.DateTimeField(auto_now_add=True, null=False)
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='purchases', on_delete=models.CASCADE)

    class Meta:
        db_table = 'purchases'
        ordering = ['-date']          # <HW37> Task 5. Sorting in ascending order

    def __str__(self):
        return f"{self.id}: {self.user.username} bought {self.book.title}({self.book.year})"
