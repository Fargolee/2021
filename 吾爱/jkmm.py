'''
Author: Lee
Descripttion: RTMart
Date: 2022-01-24 10:24:10
'''
'''
    JK
    'circle_id': 492
    JK制服
    'circle_id': 976
    JK日常
    'circle_id': 5469
    JK少女
    'circle_id': 14903
    JK私影
    'circle_id': 79246
    JK制服上新
    'circle_id': 110312
    JK正片
    'circle_id': 143389
'''

import json
import os.path
import time

import requests

url = "https://bcy.net/apiv3/common/circleFeed"

par = {
    'circle_id': 492
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
    'Referer': 'https://bcy.net/tag/492'
}

res = requests.get(url, headers=header, params=par)
res_encode = res.text.encode('utf-8')
res_json = json.loads(res_encode)

for item in res_json['data']['items']:
    name = item['item_detail']['uname']
    if not os.path.exists(f'D:\\bcy\\{name}'):
        os.makedirs(f'D:\\bcy\\{name}')
        os.chdir(f'D:\\bcy\\{name}')
    else:
        os.chdir(f'D:\\bcy\\{name}')

    avatar = item['item_detail']['avatar']
    avatar_name = str(avatar).rsplit('.image')[0]
    avatar_name1 = str(avatar_name).rsplit('/')[-1]
    print(f'{avatar_name1}.jpg')
    with open(f'{avatar_name1}.jpg', 'wb') as f1:
        f1.write(requests.get(avatar, headers=header).content)
    print(name, avatar_name1)

    for image in item['item_detail']['image_list']:
        images = image['path']
        images_name = str(images).rsplit('.image')[0]
        images_name1 = str(images_name).rsplit('/')[-1]
        with open(f'{images_name1}.jpg', 'wb') as f2:
            f2.write(requests.get(images, headers=header).content)
        print(f'{images_name1}.jpg')
    time.sleep(1)
