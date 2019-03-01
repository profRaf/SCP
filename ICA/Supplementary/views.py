import traceback
from django.http import JsonResponse
from django.shortcuts import render

def health_check(request):
    response = {'HTTPStatus':'OK', 'HTTPStatusCode':200}
    return JsonResponse(response)
