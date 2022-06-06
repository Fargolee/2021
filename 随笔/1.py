'''
Author: Lee
Descripttion: Myhome
Date: 2022-05-29 16:22:30
'''
import json
i =  [{'id': 30, 'merchants_id': 30, 'store_name': '测试', 'province_code': 110000, 'city_code': 110100, 'region_code': 110102, 'address': '测试', 'all_address': '北京北京市西城区测试', 'charge_people': '测试', 'charge_phone': '18212341234', 'join_time': datetime.datetime(2020, 12, 2, 0, 0), 'create_time': datetime.datetime(2020, 12, 23, 15, 8, 14), 'create_user': None, 'update_time': None, 'update_user': None, 'is_true': 1, 'status': 1, 'qr_code': '/upload/qrCode/6d692c74f39b4958a82a3b957e8884d6.png'}]

a = json.dumps(i)
print(a)