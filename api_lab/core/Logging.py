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
