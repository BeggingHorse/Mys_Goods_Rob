import requests as r

params = {
    "title":"米游社商店兑换简况"
}

def serverchan(msg,SCTKEY)->None:
    url = f"https://sctapi.ftqq.com/{SCTKEY}.send"
    params["desp"] = msg
    r.post(url=url,params=params)