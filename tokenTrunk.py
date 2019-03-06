#!/user/bin/env python
#coding=utf-8
import json

import requests

def test():
    url = "https://kf-wdy-trunk.wjs-test.com/wdy/api/usermanage/v1/login"  #登录的接口
    #headers = {'content-type': 'application/json'}
    headers = {'content-type': 'text/html'}
    data={'username':'zhangsan','password':'123','d_code':'000000'}
    r = requests.post(url=url, headers=headers,params=data)
    print r.headers['x-auth-token']


test()
