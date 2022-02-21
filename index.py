from tracemalloc import start
import requests as r
import json
import time
from info import info
from config.config import config
from push.send import send


def main_handler(event, context):
    start_time = time.time()
    rmsg = rob()
    end_time = time.time()
    msg = getmsg(start_time=start_time, end_time=end_time, rmsg=rmsg)
    send(msg=msg,config=config.send)
    print(msg)
    return rmsg

def rob(times = 100):
    global rob_times
    url = "https://api-takumi.mihoyo.com/mall/v1/web/goods/exchange"
    exit_retcode = [0, -2109, -2007, -2103]
    for rob_times in range(times):
        rmsg = r.post(url=url,headers=config.headers,params=config.params)
        rmsg = json.loads(rmsg.text)
        retcode = rmsg["retcode"]
        if retcode in exit_retcode:
            break
    rob_times += 1 
    return rmsg

def getmsg(start_time,end_time,rmsg):
    retcode = rmsg["retcode"]
    message = rmsg["message"]
    goods_id = config.params["goods_id"]
    good_info = info.good(goods_id)
    cover = good_info["cover"][0]["url"]
    goods_name = good_info["goods_name"]
    
    try:
        try:order_sn=rmsg["order_sn"]
        except:order_sn=rmsg["data"]["order_sn"]
    except:order_sn = None

    smsg=f'''
## {time.ctime(start_time)}—
## {time.ctime(end_time)}  
> 耗时：{end_time-start_time:.5f}   
***
```
目标商品：{goods_name}  
retcode：{retcode}  
message：{message}  
订单号：{order_sn}  
请求次数：{rob_times}
```
![Image]({cover})
    '''
    return smsg
