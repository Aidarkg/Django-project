from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")


def data_view(request):
    if request.method == 'GET':
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"Current date and time: {formatted_date}")


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")
