from time import strftime, localtime
import os
from datetime import date, timedelta

def save_log():

    yesterday = date.today()
    date_file = yesterday.strftime("%Y-%m-%d")
    date_time = strftime("%H-00-00", localtime())
    filename = "api_lab/log/"+date_file+"/"+date_time+".log"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "a+") as f:
        datetime = strftime("%Y-%m-%d %H:%M:%S", localtime())
        f.write("[" + datetime + "] Derta Isyajora\n")

def save_log_middleware_before(array_param):

    yesterday = date.today()
    date_file = yesterday.strftime("%Y-%m-%d")
    date_time = strftime("%H-00-00", localtime())
    filename = "api_lab/log/"+date_file+"/"+date_time+".log"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "a+") as f:
        datetime = strftime("%Y-%m-%d %H:%M:%S", localtime())
        f.write("[" + datetime + "] Log from Middleware Before "+"[Method : "+ array_param[1] +"] [URL Source : "+ array_param[0] + "] [Data Received :"+array_param[2]+"]\n")


def save_log_middleware_after(array_param):

    yesterday = date.today()
    date_file = yesterday.strftime("%Y-%m-%d")
    date_time = strftime("%H-00-00", localtime())
    filename = "api_lab/log/"+date_file+"/"+date_time+".log"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "a+") as f:
        datetime = strftime("%Y-%m-%d %H:%M:%S", localtime())
        f.write("[" + datetime + "] Log from Middleware After "+"[Method : "+ array_param[1] +"] [URL Source : "+ array_param[0] + "] [Data Sent :"+array_param[2]+"]\n")
