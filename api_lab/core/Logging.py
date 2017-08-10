from time import strftime, localtime
import os
from datetime import date, timedelta
import logging

def save_log():

    yesterday = date.today()
    date_file = yesterday.strftime("%Y-%m-%d")
    date_time = strftime("%H-00-00", localtime())
    filename = "api_lab/log/"+date_file+"/"+date_time+".log"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "a+") as f:
        datetime = strftime("%Y-%m-%d %H:%M:%S", localtime())
        f.write("[" + datetime + "] Derta Isyajora\n")

def save_log_event(array_param):

    yesterday = date.today()
    date_file = yesterday.strftime("%Y-%m-%d")
    date_time = strftime("%H-00-00", localtime())
    filename = "api_lab/log/"+date_file+"/"+date_time+".log"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "a+") as f:
        datetime = strftime("%Y-%m-%d %H:%M:%S", localtime())
        # "T2", "INQ", "IN", "Inquiry req ext", "SUB ID", "REF ID", product, request
        f.write("[" + datetime + "][INFO]["+array_param[1]+"]["+array_param[0]+" "+array_param[2]+" "+ array_param[3]+"]"+"["+array_param[4]+"]"+"["+array_param[5]+"]["+ array_param[0] + "]["+array_param[7]+"]\n")

def save_log_middleware_before(array_param):

    yesterday = date.today()
    date_file = yesterday.strftime("%Y-%m-%d")
    date_time = strftime("%H-00-00", localtime())
    filename = "api_lab/log/"+date_file+"/"+date_time+".log"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "a+") as f:
        datetime = strftime("%Y-%m-%d %H:%M:%S", localtime())
        f.write("[" + datetime + "][INFO]["+array_param[3]+"][T1 IN "+ array_param[4] +" Apy][][]["+ array_param[0] + "]["+array_param[2]+"]\n")


def save_log_middleware_after(array_param):

    yesterday = date.today()
    date_file = yesterday.strftime("%Y-%m-%d")
    date_time = strftime("%H-00-00", localtime())
    filename = "api_lab/log/"+date_file+"/"+date_time+".log"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "a+") as f:
        datetime = strftime("%Y-%m-%d %H:%M:%S", localtime())
        f.write("[" + datetime + "][INFO][" + array_param[3] + "][T6 OUT " + array_param[4] + " Apy][][][" + array_param[
            0] + "][" + array_param[2] + "]\n")
