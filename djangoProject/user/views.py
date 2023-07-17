from user.models import User
from django.http import HttpResponse, JsonResponse


# <HW37> Task 4. JSON response
def json_users(request):
    if request.method == "GET":
        response_list = list(User.objects.all().values())

        return JsonResponse(response_list, safe=False)
