from celery import shared_task
from purchase.models import Purchase
from users.models import User

# <HW42> Task3. Celery task to print any text
@shared_task()
def print_any_text():
    print('Print any text')


@shared_task
def user_purchases(user_id):
    queryset = Purchase.objects.all().filter(user_id=user_id)
    p_qty = len(queryset)
    print(f"User {user_id} has {p_qty} purchases")

@shared_task
def users_qty():
    queryset = User.objects.all()
    users_qty = len(queryset)
    print(f"There are {users_qty} users")