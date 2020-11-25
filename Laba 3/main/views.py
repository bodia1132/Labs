from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime


def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    now = datetime.now()
    response = {'date': now.strftime("%d/%m/%Y %H:%M:%S"), 'current_page': request.build_absolute_uri(), 'server_info': os.uname(), 'client_info': request.headers['User-Agent']}
    return JsonResponse(response)
