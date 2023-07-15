from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse(
        """
        <div class='container'>
        <h1>HELLO WORLD</h1>
        <div>
        """
    )