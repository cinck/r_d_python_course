from book.models import Book
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# <HW37> Task 4. JSON response
def json_books(request):
    if request.method == "GET":
        response_list = list(Book.objects.all().values())
        return JsonResponse(response_list, safe=False)
