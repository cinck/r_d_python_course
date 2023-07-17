from purchase.models import Purchase
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# <HW37> Task 4. JSON response
def json_purchases(request):
    if request.method == "GET":
        response_list = list(Purchase.objects.all().values())

        return JsonResponse(response_list, safe=False)


def hello_(request):
    return HttpResponse(
        f"""
        <div class='container'>
        <h1>HELLO. It's {__name__} page!</h1>
        <div>
        """
    )
