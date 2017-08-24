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
from . import logging_main as log_new

from .models import Product

import json

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

@api_view(['GET','POST'])
def logging_example(request, format=None):

    resp = {'result_code': '0', 'resut_message': 'Payment Success'}
    # HANDMADE
    log_param = ["INFO","T2","IN", "INQ Inquiry req ext (Subscriber ID) ", resp, request.get_full_path(), request.method]
    log_new.save_log_event(log_param)

    # BUILT IN FROM DJANGO
    log_new.logger.warning("[%s] [%s]","T2 INQ Inquiry req ext (Subscriber ID)","Response Data :" + json.dumps(resp))
    log_new.logger.error("[%s] [%s] [%s]","TESTING LOG" ,"T2 INQ Inquiry req ext (Subscriber ID)", "Response Data :" + json.dumps(resp))
    log_new.logger.info("[%s] [%s]", "T2 INQ Inquiry req ext (Subscriber ID)", "Response Data :" + json.dumps(resp))

    resp = {'result_code': '0', 'result_message': 'Success', 'data': "test"}
    return Response(resp)

@api_view(['GET'])
def learn_curl(request):
    token = cred.token_server_uber_api()
    data_product_uber = Uber.get_product_data(token)
    resp = {'result_code': '0', 'result_message': 'Success', 'data': data_product_uber}
    return Response(resp)