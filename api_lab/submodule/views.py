
from django.http import HttpResponse

# django rest framework
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def example_method(request):

    resp = {'result_code': '0', 'resut_message': 'Success', 'data': 'test'}
    return Response(resp)