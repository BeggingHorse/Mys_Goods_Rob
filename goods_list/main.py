from info import info
import os
import json
def clear():
    os.system('cls')

def main(good_id,cookie):

    def input_index(list):
        try:
            index = int(input("\n请输入数字选择："))
            account = list[index]
            clear()
            return index
        except:
            print('请输入一个正确的数字！')
            index = input_index(list)
            return index

    def choose_account(accounts):
        print('请选择账号...\n')
        print('===================\n')
        info_sequence = ('nickname','game_uid','level','region_name')
        info_dict = {'nickname':'昵称','game_uid':'uid','level':'等级','region_name':'服务器'}
        for account in accounts:
            print(f'\n-------{accounts.index(account)}-------')
            for key in info_sequence:
                try:
                    msg = f'{info_dict[key]}：{account[key]}'
                    print(msg)
                except: return accounts
        account_index = input_index(accounts)
        account = accounts[account_index]
        return account

    def choose_addr(cookie,is_default = 0):
        info_sequence = ('connect_name','connect_mobile','province_name','city_name','county_name','addr_ext')
        addrs = info.addr(cookie=cookie)
        print('请选择地址...\n')
        for addr in addrs:
            if addr['is_default']==1 and is_default == 1:
                return addr['id']
            print(f'========{addrs.index(addr)}=========\n')
            for key in info_sequence:
                msg = addr[key]
                print(msg)
        addr_index = input_index(addrs)
        clear()
        return addrs[addr_index]['id']

    def write_config(cookie = None,goods_id = None,uid = None,
    region="cn_gf01",game_biz="hk4e_cn",address_id = None,
    exchange_num = 1):
        config = {
            'cookie':cookie,
            'goods_id':goods_id,
            'uid':uid,
            'region':region,
            'game_biz':game_biz,
            'address_id':address_id,
            'exchange_num':exchange_num
        }
        with open('config.json','w+') as f:
            json.dump(config,f,indent=2)

    good_info ,accounts = info.go(good_id=good_id,cookie=cookie)
    game_biz = good_info['game_biz']
    addr = choose_addr(cookie=cookie)
    region = ''
    try:
        account = choose_account(accounts=accounts)
        uid = account['game_uid']
        region = account['region']
    except:
        uid = account
        pass
    write_config(cookie=cookie,goods_id=good_id,uid=uid,region=region,game_biz=game_biz,address_id=addr)
