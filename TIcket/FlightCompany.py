#coding:utf-8

import requests
import hashlib


def Test():
    url = 'http://api.tripsky.com.cn/ctrip/API/ctripPolicy.php'
    data = {
        'username': "KKKKKKK",
        'password': "XXXXXXX",
        'startDate': "2018-01-01",
        'endDate': "2018-01-02",
        'depcity': "FOC",
        'arrcity': "CTU",
        'code2': "MF",
    }

    # 获取sign
    sign = ''
    for i in data.values():
        sign += i

    # 使用md5加密
    sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
    print(sign)

    # 将sign添加到data字典
    data['sign'] = sign
    print(data)

    # 发送post请求
    response = requests.post(url, data=data).content
    print(response)
    return response


Test()

