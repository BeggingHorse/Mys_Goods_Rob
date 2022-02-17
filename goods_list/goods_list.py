import json
import requests
import time
import ctypes
import os
ctypes.windll.kernel32.SetConsoleTitleW('米游社商品清单')

def clear():
    os.system('cls')

def get_list(key:str)-> list:
    url='https://api-takumi.mihoyo.com/mall/v1/web/goods/list'
    headlers={
    'Host': 'api-takumi.mihoyo.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://user.mihoyo.com',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; MI NOTE Pro Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36 miHoYoBBS/2.12.1',
    'x-rpc-client_type': '5',
    'x-rpc-device_id': '58cb65c8-463f-4503-8389-cd2ff1d7d36f',
    'Referer': 'https://webstatic.mihoyo.com/app/community-shop/index.html?bbs_presentation_style=no_header',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'Cookie': '', 
    'X-Requested-With': 'com.mihoyo.hyperion'
    }
    got_list = [1]
    return_list = []
    page = 1
    while got_list != []:
        params={
        'app_id':'1',
        'point_sn':'myb',
        'page_size':'20',
        'page':page,
        'game':key
        }
        r = requests.get(url=url,headers=headlers,params=params)
        msg = json.loads(r.text)
        got_list = msg["data"]["list"]
        return_list = return_list+got_list
        page += 1
    return return_list

def get_key_info(goods_list:list)-> list:
    del_element = ['app_id','type','point_sn','icon',
    'unlimit','total','account_cycle_type',
    'account_cycle_limit','account_exchange_num',
    'role_cycle_type','role_cycle_limit','role_exchange_num',
    'status','next_num','now_time']
    return_list = []
    for good in goods_list:
        for Del in del_element:
            del good[Del]
        return_list.append(good)
    return return_list

def search(goods_name_list):
    key_word = input("在此输入关键词：")
    key_word_list = []
    for GoodName in goods_name_list:
        if key_word in GoodName:
            key_word_list.append(GoodName)
    return key_word_list

def main():
    clear()
    goods_type=('bh3','hk4e','bh2','nxx','bbs','')
    goods_dict={'':'全部商品','bh3':'崩坏三','hk4e':'原神','bh2':'崩坏二','nxx':'未定事件簿','bbs':'米游社'}
    print('选择商品分区！\n')
    print('===================\n')
    for good_type in goods_type:
        print(f"{goods_type.index(good_type)} --  {goods_dict[good_type]}")
    try:
        index = int(input("\n输入数字选择分区："))
        goods_list = get_key_info(get_list(goods_type[index]))
    except:
        clear()
        print('请输入一个正确的数字！')
        main()
    goods_name_list = []
    for good_name in goods_list:
        good_name = good_name['goods_name']
        goods_name_list.append(good_name)
    
    def get_good_info(GoodName):
        for good in goods_list:
            if good['goods_name'] == GoodName:
                return good

    def print_goods_list(num = 1):
        if num == 0:
            print('\n-1 -- 返回上级')
            print('-2 -- 使用关键词搜索商品')
            return
        clear()
        print('\n发现以下商品...\n')
        print('===================\n')
        for GoodName in goods_name_list:
            print(f'{goods_name_list.index(GoodName)} --  {GoodName}')
        print('\n-1 -- 返回上级')
        print('-2 -- 使用关键词搜索商品')
    
    def choose_good(num = 1):

        def input_index()->int:
            try:
                print_goods_list(num)
                good_index = int(input("\n请输入数字选择："))
                if type(good_index) == int :
                    return good_index
            except:
                clear()
                print('请输入一个正确的数字！')
                good_index = input_index()
                return good_index

        good_index = input_index()
        if good_index == -1:
            print()
            main()

        elif good_index == -2:
            key_word_list = search(goods_name_list)
            clear()
            print("\n以下是查询结果...")
            print('===================\n')
            for GoodName in key_word_list:
                print(f'{goods_name_list.index(GoodName)} --  {GoodName}')
            choose_good(0)
        else:
            try:
                print('\n你选择了 '+goods_name_list[good_index])
                good_info = get_good_info(goods_name_list[good_index])
                clear()
                print_info(good_info)
            except:
                print('请输入一个正确的数字！')
                print_goods_list()
                choose_good()

    def print_info(good_info):
        info_dict = {'goods_name':'商品名称','goods_id':'商品编号','price':'价    格',
        'start':'开始时间','end':'结束时间','next_time':'下次开始时间'}
        info_sequence = ('goods_name','goods_id','price') # ,'next_time','start','end'
        start = int(good_info['start'])
        end = int(good_info['end'])
        next_time = int(good_info['next_time'])
        print()
        for key in info_sequence:
            msg = '{}：\t{}'.format(info_dict[key],good_info[key])
            print(msg)
        if next_time == 0:
            next_time_msg = '常驻商品，现在可兑换'
        else:
            next_time_msg = time.ctime(next_time)
        print('下次开始时间：\t{}'.format(next_time_msg))
        print()
        print('兑换持续时间：\t从 {} 起开始，至 {} 结束...'.format(time.ctime(start),time.ctime(end)))

    print_goods_list()
    choose_good()

    
try:
    main()
    time.sleep(5)
    print()
    input("按 Enter 关闭...")
except:
    time.sleep(5)
    print()
    input("按 Enter 关闭...")