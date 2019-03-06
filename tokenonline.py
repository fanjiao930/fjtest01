#!/user/bin/env python
#coding=utf-8
import json

import requests

def test():
    url = "https://kf-wdy-online.wjs-test.com/wdy/api/usermanage/v1/login"  #登录的接口
    #headers = {'content-type': 'application/json'}
    headers = {'content-type': 'text/html'}
    data={'username':'zhangsan','password':'123','d_code':'000000'}
    r = requests.post(url=url, headers=headers,params=data)
    print r.headers['x-auth-token']


'''
def test_have_session():
    url='http://kf-api-online.wjs-test.com/wdy.openapi.api/mockReqGenerator.do'
    headers = {'content-type': 'application/json'}
    data={'appId':'souche','charset':'utf-8','version':'1.0.0','service':'carDasProductRelease','bizParamsJson':'','appPublicKey':'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3GFaW5S8GI7ejxhnVjhC6is3k5ZXY','appPrivateKey':'MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDcYVpblLwYjt6PGGdWOELqKzeTlldj54cruFXjZbtpI','wjsPublicKey':'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAneBTIR72RkQQDLkap9GZr7zRQZGMhrH/TTmkvgjAIBweIm/nIgxN5Qn2GR4YtL1dojDASGp8GjXr+HNLruFsnhS0JDAFG4Fv4iKPqUfMaHI6PUT7E8TdCDi+CqUnkyzNjEGSp8n3wboKCLdeZmc84o+pXF8tgiP9sHDSoODcOr9YmfBLfsBIKpT1XgEmkwBUo5iTUJ+GiMvBac5ZfAAz/Z3lEAjDlhvO5Q21PUQrNGKgBX6OtTMmI/imyL4VsMsnGSSKyhcCrBJ+LVYgeVBXoET+A4EoxM6v4Jb58IFTQQ4mBTimfJapEvm34RwQPsPl/nydgk2pSpt/jWUx2Hl+QwIDAQAB','wjsPrivateKey':'MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCd4FMhHvZGRBAMuRqn0ZmvvNFBkYyGsf9NOaS','openApiUrl':'http://kf-api-trunk.wjs-test.com/wdy.openapi.api/gateway.do'}
    r1 = requests.post(url=url, headers=headers,params=data)
    #print r1.headers['x-auth-token']
    #print r1.json()'''

test()
