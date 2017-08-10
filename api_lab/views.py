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
from .core import Credential as cred

#load API from third party
from .api_external import Uber

#load python library in same directory
from . import Laboratorium as test

from .models import Product

def home(request):
    return HttpResponse ('Hello World!!')

def derta(request):
    return HttpResponse ('Hello Derta!!')


@api_view(['POST','GET'])
def product(request):
    derta = test.test_nilai()
    resp = {'result_code': '0', 'resut_message': 'Success', 'product_data': 33,
            'purchase_data': 11, 'nilai' : derta}
    return Response(resp)

@api_view(['GET'])
def traditional_logging(request):
    log_api.save_log()
    return Response("Write log success")

@api_view(['GET'])
def use_model(request):
    product = Product.objects.filter(product_id=1,).values()
    # product = Product.objects.all().values()
    log_api.save_log_event("T2", "INQ", "IN", "Inquiry req ext", "SUB ID", "REF ID", product, request)
    # print(product.product_id)
    # print(product.product_name)
    resp = {'result_code': '0', 'result_message': 'Success', 'data': list(product)}
    return Response(resp)

@api_view(['GET'])
def learn_curl(request):
    token = cred.token_server_uber_api()
    data_product_uber = Uber.get_product_data(token)
    resp = {'result_code': '0', 'result_message': 'Success', 'data': data_product_uber}
    return Response(resp)