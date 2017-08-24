from time import strftime, localtime
import os
from datetime import date, datetime
import logging
import json

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
yesterday = date.today()
date_file = yesterday.strftime("%Y-%m-%d")
date_time = strftime("%H-00-00", localtime())
filename = "api_lab/log/" + date_file + "/" + date_time + ".log"
os.makedirs(os.path.dirname(filename), exist_ok=True)

# LOG FROM Django
FORMAT = '[%(asctime)-15s][%(levelname)s][File: %(filename)s, Function: %(funcName)s]%(message)s'
logging.basicConfig(filename=filename, format=FORMAT)
logger = logging.getLogger('logger.out')


def current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    return current_time

# LOG HANDMADE
def save_log_event(array_param):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
    with open(filename, "a+") as f:
        if(array_param[2] == "IN"):
            text_data = "data receive :"
        else:
            text_data = "data sent :"
        f.write("[" + current_time +"]["+array_param[6]+": "+array_param[5]+"]["+array_param[0]+"]["+array_param[1]+" "+ array_param[3] + "]["+text_data+" "+json.dumps(array_param[4])+"]\n")
