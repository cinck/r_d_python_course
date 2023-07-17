from purchase.models import Purchase
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# <HW37> Task 4. JSON response
def json_purchases(request):
    if request.method == "GET":
        response_list = list(Purchase.objects.all().values())

        return JsonResponse(response_list, safe=False)
