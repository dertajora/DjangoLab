from django.shortcuts import render
from django.http import HttpResponse

# django rest framework
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.views import APIView

#load my own python code from another directory
from .core import Logging as log_api

def home(request):
    return HttpResponse ('Hello World!!')

def derta(request):
    return HttpResponse ('Hello Derta!!')


@api_view(['POST','GET'])
def product(request):
    resp = {'result_code': '0', 'resut_message': 'Success', 'product_data': 33,
            'purchase_data': 11}
    return Response(resp)

@api_view(['GET'])
def traditional_logging(request):
    log_api.save_log()
    return Response("Write log success")