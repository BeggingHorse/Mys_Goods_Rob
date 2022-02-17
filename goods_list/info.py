import requests
import json
class Info:
    def __init__(self) -> None:
        pass

    def good(self,good_id):
        url='https://api-takumi.mihoyo.com/mall/v1/web/goods/detail'
        headler={
        'Host': 'api-takumi.mihoyo.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://webstatic.mihoyo.com',
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 miHoYoBBS/2.7.0",
        'Referer': 'https://webstatic.mihoyo.com/app/community-shop/index.html?bbs_presentation_style=no_header',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8',
        'Cookie': "",
        'X-Requested-With': 'com.mihoyo.hyperion',
        }
        params={
        'app_id':'1',
        'point_sn':'myb',
        'goods_id':good_id
        }
        r=requests.get(url=url,headers=headler,params=params)
        info = json.loads(r.text)['data']
        del_elements = ['app_id','type','point_sn','icon',
        'unlimit','total','account_cycle_type',
        'account_exchange_num',
        'role_cycle_type','role_cycle_limit','role_exchange_num',
        'status','next_num','now_time','goods_name','goods_desc',
        'goods_detail','cover','rules','price','start','end',
        'bbs_detail','sale_start_time']
        for del_element in del_elements:
            del info[del_element]
        return info

    def player(self,cookie,game_biz):
        url = f'https://api-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie?game_biz={game_biz}'
        headers = {
            'cookie' : cookie
        }
        r = requests.get(url=url,headers=headers)
        accounts = json.loads(r.text)['data']['list']
        return accounts

    def addr(self,cookie):
        url = 'https://api-takumi.mihoyo.com/account/address/list'
        headers = {
            'cookie': cookie
        }
        info = requests.get(url=url,headers=headers)
        addrs = json.loads(info.text)['data']['list']
        addrr = []
        del_element = ['connect_areacode','country','province','city','county','status']
        for addr in addrs:
            for key in del_element:
                del addr[key]
        return addrs

    def go(self,good_id,cookie):
        self.good_info = self.good(good_id=good_id)
        self.game_biz = self.good_info['game_biz']
        self.accounts = self.player(cookie=cookie,game_biz=self.game_biz)
        return self.good_info , self.accounts

info = Info()