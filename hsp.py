#!/usr/bin/python
# -*- coding: utf-8 -*-

# 生成对外接口业务参数 Json 字符串


import json


def carDasProductReleaseBizParams():

    bizParams = {}

    bizParams["financingNo"] = "HUASHENG-LXX20181026001" #产品融资编号，唯一
    bizParams["productName"] = "花生分子公司统计_LXX20181026001号" #产品名称，唯一
    bizParams["requestAmount"] = "364000"  #申请融资金额
    bizParams["carriageDate"] = "20181026"  #上架日期，需大于等于推送日期，一般为推送日期的下一自然日
    bizParams["underDate"] = "20181026"  #下架日期，默认等于上架日期
    bizParams["valueDate"] = "20181027"  #起息日，需为下架日的下一自然日
    bizParams["term"] = "365"  #期限：期限=到期日–起息日
    bizParams["dueDate"] = "20191027"  #到期日
    bizParams["minPreDueDate"] = "20190928"  #最早可提前还款日=到期日-29天
    bizParams["profitYearRate"] = "0.088"  #发行利率
    bizParams["bizType"] = "HSHC"  # 业务类型，默认HSHC-花生好车
    bizParams["issuePeriods"] = "12"  #发行期数，起息日+发行期数个月=到期日
    


    print ("Params-carDasProductRelease: \n"  + json.dumps(bizParams) +  "\n")


carDasProductReleaseBizParams()





