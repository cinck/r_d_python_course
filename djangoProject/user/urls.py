
from django.urls import path
from user import views


urlpatterns = [
    path('', views.hello_world)
]