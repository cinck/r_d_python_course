from user.models import User
from django.http import HttpResponse, JsonResponse


def json_users(request):
    if request.method == "GET":
        response_list = list(User.objects.all().values())

        return JsonResponse(response_list, safe=False)


def hello_(request):
    return HttpResponse(
        f"""
        <div class='container'>
        <h1>HELLO. It's {__name__} page!</h1>
        <div>
        """
    )
