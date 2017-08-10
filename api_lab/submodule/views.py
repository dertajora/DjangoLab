
from django.http import HttpResponse

# django rest framework
from rest_framework.response import Response
from rest_framework.decorators import api_view

import logging

from time import strftime, localtime
from datetime import date, timedelta
# import os

logger = logging.getLogger(__name__)

@api_view(['GET'])
def example_method(request):
    yesterday = date.today()
    date_file = yesterday.strftime("%Y-%m-%d")
    date_time = strftime("%H-00-00", localtime())
    filename = "api_lab/log/" + date_file + "/" + date_time + ".log"
    logging.basicConfig(filename=filename, level=logging.DEBUG)
    logger.info('AMS_TRY|openid:%s|item_id:%s|package_id:%s|serial:%s|' % (1, 2, 3, 4))



    resp = {'result_code': '0', 'resut_message': 'Success', 'data': 'test'}
    logger.error('AMS_TRY|openid:%s|item_id:%s|package_id:%s|serial:%s|' % (1, 2, 3, 4))
    logger.debug('AMS_TRY|openid:%s|item_id:%s|package_id:%s|serial:%s|' % (1, 2, 3, 4))


    return Response(resp)



