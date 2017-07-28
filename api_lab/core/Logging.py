from time import strftime, gmtime
import os
from datetime import date, timedelta

def save_log():

    yesterday = date.today()
    date_file = yesterday.strftime("%Y-%m-%d")
    date_time = strftime("%H-00-00", gmtime())
    filename = "api_lab/log/"+date_file+"/"+date_time+".log"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "a+") as f:
        datetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        f.write("[" + datetime + "] Derta Isyajora\n")

def save_log_middleware(array_param):

    yesterday = date.today()
    date_file = yesterday.strftime("%Y-%m-%d")
    date_time = strftime("%H-00-00", gmtime())
    filename = "api_lab/log/"+date_file+"/"+date_time+".log"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "a+") as f:
        datetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        f.write("[" + datetime + "] Log from Middleware"+"[Method : "+ array_param[1] +"] [URL Source : "+ array_param[0] + "] [Data Received :"+array_param[2]+"]\n")
