import datetime
import pytz
import json
import os
import asyncio
import time
import logging
import traceback


def standard_time():
    now = datetime.datetime.now()
    new_timezone = pytz.timezone('Asia/Tokyo')
    new_now = now.astimezone(new_timezone)
    # print(new_now,"is current time in Japan")
    return new_now

def current_week():
    now = standard_time()
    return now.isocalendar().week

def current_month():
    now = standard_time()
    return now.month

if(__name__ == "__main__"):
    print(current_month())
    # result = standard_time()
    # with open(os.path.abspath(os.path.dirname(__file__))+'\config.json','r+', encoding='UTF-8') as f:
    #     data=json.loads(f.read())
    #     datetime_object = datetime.datetime.strptime(data["weekly"]["last_date"], '%Y-%m-%d %H:%M:%S')
    #     print(datetime_object.isocalendar())
        # data["weekly"]["last_date"] = result.strftime('%Y-%m-%d %H:%M:%S')
        # f.seek(0)
        # json.dump(data, f, indent=4)
        # f.truncate()