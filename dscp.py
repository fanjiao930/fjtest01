#!/usr/bin/python
# -*- coding: utf-8 -*-

# 生成对外接口业务参数 Json 字符串


import json


def carDasProductReleaseBizParams():

    bizParams = {}

    bizParams["financingNo"] = "DSCFJ201811060009"#产品代码：姓名标识+DSC+XX（某月）+XX（某日）+XX（号）
    bizParams["productName"] = "弹个车新车-DSCFJ201811060009号"#产品名称：产品标识+XX（年）+XX（月）++XX（日）+XXX号，其中年月日和产品代码对应
    bizParams["requestAmount"] = "1000000"#申请融资金额
    bizParams["carriageDate"] = "20181108”#上架日期
    bizParams["underDate"] = “20181108”#下架日期，下架日期=上架日期
    bizParams["valueDate"] = “20181109”#起息日，起息日=下架日期+1天
    bizParams["term"] = "365"#期限，期限=到期日-起息日
    bizParams["dueDate"] = "20191109”#到期日=租约结束日+30天 20190111
    bizParams["minPreDueDate"] = "20191011” #最早可提前还款日，最早可提前还款日必须=到期日-29天，最早可提前还款日=租约到期日
    bizParams["profitYearRate"] = "0.099"#发行利率
    bizParams["bizType"] = "TGC"#TGC-弹个车新车，TGC_SECOND_HAND-弹个车二手车
    bizParams["assetNum"] = "1"#产品对应资产数
    


    print ("Params-carDasProductRelease: \n"  + json.dumps(bizParams) +  "\n")


carDasProductReleaseBizParams()





