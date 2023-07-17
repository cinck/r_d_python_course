
from django.http import HttpResponse
from django.shortcuts import render


def hello_(request):
    return HttpResponse(
        f"""
        <div class='container'>
        <h1>HELLO. It's {__name__} page!</h1>
        <div>
        """
    )