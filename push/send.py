import json
from .ServerChan import serverchan

send_dict = {"SCTKEY":serverchan}
SendKeys = list(send_dict.keys())

def send(config,msg):
    ConfigKeys = list(config.keys())
    for SendKey in SendKeys:
        if SendKey in ConfigKeys:
            SENDKEY = config[SendKey]
            sendmsg = send_dict[SendKey]
            sendmsg(msg,SENDKEY)