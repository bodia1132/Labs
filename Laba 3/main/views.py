from django.shortcuts import render
from django.http import JsonResponse
import os
import datetime


def main(request):
    return render(request, 'main.html')


def health(request):
    response = {
        'date': datetime.datetime.now(),
        'current_page': request.build_absolute_uri(),
        'server_info': os.name,
        'client_info': request.META['HTTP_USER_AGENT']
    }
    return JsonResponse(response)
