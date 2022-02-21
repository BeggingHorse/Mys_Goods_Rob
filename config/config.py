import os
import json

class Config:

    try:
        with open('./config/config.json','r') as f:
            config = json.load(f)
        for key in list(config.keys()):
            if not config.get(key):
                del config[key]
    except:
        pass

    send = {}

    params = {
            "app_id": "1",
            "point_sn": "myb"
        }

    headers = {
        "Host": "api-takumi.mihoyo.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://user.mihoyo.com",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 miHoYoBBS/2.7.0",
        "x-rpc-client_type": "5",
        "x-rpc-device_id": "7dab6a2c-b917-4184-8da5-cffd45c085fc",
        "Referer": "https://user.mihoyo.com/?hideTitle=true&bbs_show_back=true",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,en-US;q=0.8"
        }
    
    def __init__(self) -> None:
        self.Cookie()
        self.Params()
        self.Headers()
        self.ServerChan()
        pass

    def Cookie(self) -> None:
        try:
            self.cookie = os.environ['cookie']
        except:
            try: self.cookie = self.config['cookie']
            except: 
                print('缺失参数Cookie，结束！')
                exit()
        
    def Params(self) -> None:
        key_words = ["goods_id","exchange_num","uid","region","game_biz","address_id"]
        for key_word in key_words:
            try:
                self.params[key_word] = os.environ[key_word]
            except:
                try: self.params[key_word] = self.config[key_word]
                except: pass

        for key in ["goods_id","exchange_num","uid","game_biz","address_id"]:
            if key not in list(self.params.keys()):
                print(f"缺失参数{key}，结束！")
                exit()

    def Headers(self) -> None:
        self.headers['Cookie'] = self.cookie

    def ServerChan(self) -> None:
        try:
            self.send["SCTKEY"] = os.environ['SCTKEY']
        except:
            try:self.send["SCTKEY"] = self.config['SCTKEY']
            except:pass

config = Config()
