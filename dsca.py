#!/usr/bin/python
# -*- coding: utf-8 -*-
import json



def carDasPushAssetBizParams():

    bizParams = {}

    bizParams["financingNo"] = “DSCFJ201811060010”#对应产品代码
    bizParams["orderNo"] = "dingdan-DSCFJ201811060010号"#资产唯一编号
    bizParams["contractNo"] = "hetong-DSCFJ201811060010号" #融资租赁协议编号
    bizParams["bizType"] = "TGC" #业务类型：TGC-弹个车新车，TGC_SECOND_HAND-弹个车二手车  库融STOCK_PLEDGE
    bizParams["orderFrom"] = "TGC"  #订单来源：TGC-弹个车APP，TMALL-天猫
    bizParams["requestDateTime"] = "1531883237000" #下单时间戳
    bizParams["pickUpDate"] = "20180101" #提车日期

    custInfo = {} #客户信息
    custInfo["name"] = "_0009可退" #购车人姓名
    custInfo["certType"] = "1" #证件类型：1-身份证
    custInfo["certNo"] = "371425199008027668" #证件号码
    custInfo["phoneNum"] = "13718498221" #电话号码 
    custInfo["alipayAccount"] = "lixinxin@ktjr.com" #支付宝账号
    custInfo["alipayUserId"] = "208800041"  #支付宝Uid
    custInfo["certFrontPic"] = "" #身份证正面照
    custInfo["certBackPic"] = "" #身份证反面照
    custInfo["drivingLicencePic"] = "" #驾驶证照片
    bizParams["custInfo"] = custInfo

    carInfo = {} #车辆信息
    carInfo["province"] = "北京" #省份
    carInfo["city"] = "朝阳" #城市
    carInfo["carTypeCode"] = "DAZONG002" #针对车型的编码，唯一的标记一种车型
	
    #carInfo["brandName"] = "长城"   #国产
    #carInfo["seriesName"] = "风骏5"    
    #carInfo["modelName"] = "2016款 风骏5 2.0T两驱进取型小双排4D20C"     
    #carInfo["year"] = "2016" 
	
    #carInfo["brandName"] = "起亚"  #残值为0
    #carInfo["seriesName"] = "起亚K3"   
    #carInfo["modelName"] = "2016款 起亚K3 1.6L 自动GL"    
    #carInfo["year"] = "2016" 

    #carInfo["brandName"] = "阿尔法罗密欧"  #残值为空
    #carInfo["seriesName"] = "Stelvio"   
    #carInfo["modelName"] = "2017款 2.0T 200HP 豪华版"    
    #carInfo["year"] = "2017" 
	
    #carInfo["brandName"] = "起亚"  #匹配，系统残值2w
    #carInfo["seriesName"] = "索兰托(进口)"   
    #carInfo["modelName"] = "2018款 索兰托(进口)L 2.0T 柴油2WD都市版 7座"    
    #carInfo["year"] = "2018" 
	
    carInfo["brandName"] = "大众"   #品牌名称
    carInfo["seriesName"] = "途观L"   #车系 
    carInfo["modelName"] = "2018款 改款 330TSI 自动两驱青春版 国V"  #车型
    carInfo["year"] = "2018" 	#年份
	
    carInfo["vinCode"] = "LSVFP20181030005"  #汽车vin码
    carInfo["plateNumber"] = "苏 A32347" #车牌号：苏 A22347
    carInfo["guidePrice"] = "201000.00" #厂商指导价
    carInfo["marketPrice"] = "82900.00" #市场指导价
    carInfo["purchasePrice"] = "5" #采购基准价
    carInfo["purchasTax"] = "3"  #购置税
    carInfo["gpsFee"] = "1"   #GPS费用
    carInfo["licenseFee"] = "2"  #上牌费
    carInfo["secondHandHandleFee"] = "50000"  #二手车处置费
    carInfo["insuranceFee"] = "1"   #保险费用
    carInfo["totalCost"] = "216000"  #总成本
    carInfo["syInsuranceOrgName"] = "阳光保险"#商业保险公司
    carInfo["syInsuranceNo"] = "11556050720170219900802"#商业险保单号
    carInfo["syInsurantCode"] = "91130602MA07KD3U2U"  #商业被保险人社会统一信用代码
    carInfo["syInsurantName"] = "捷众普惠国际融资租赁有限公司安顺分公司"#商业险被保险人名称
    carInfo["syInsuranceFee"] = "12"  #商业险保费
    carInfo["syInsurancePic"] = "11rr"  #商业险保单图片
    carInfo["jqInsuranceOrgName"] = "阳光保险"#交强险保险公司
    carInfo["jqInsuranceNo"] = "11556050720170219910909"#交强险保单号
    carInfo["jqInsurantCode"] = "91130602MA07KD3U2U" #交强险被保险人社会统一信用代码
    carInfo["jqInsurantName"] = "捷众普惠国际融资租赁有限公司安顺分公司"#交强险被保险人名称
    carInfo["jqInsuranceFee"] = "1"  #交强险保费
    carInfo["jqInsurancePic"] = "22rr"  #交强险险保单图片
    carInfo["gpsSourceOrg"] = "博实结" #有源GPS供应商
    carInfo["gpsSoureCode"] = "14142905531"  #有源GPS代码
    carInfo["gpsNonSourceOrg"] = "博实结" #无源GPS供应商
    carInfo["gpsNonSourceCode"] = "14142907267"  #无源GPS代码
    carInfo["registerCert"] = "362430199303060003"  #车辆登记证
    carInfo["drivingPermitCert"] = "驾照"   #车辆行驶证
    carInfo["carTax"] = "1"  #车船税
    carInfo["secondHandTradePrice"]=""#二手车交易价格
    carInfo["maxSecondHandTradePrice"]=""#二手车交易价格上限
    carInfo["minSecondHandTradePrice"]=""#二手车交易价格下限，不生效
    carInfo["maxRestAmount"]=""#尾款金额上限
    carInfo["minRestAmount"]=""#尾款金额下限
    carInfo["secondHandOrgName"]=""#二手车商
    carInfo["secondHandOrgCode"]=""#二手车商code  验证这个
    carInfo["firstLicenseDate"]=""#首次上牌日
    carInfo["travelledDistance"]=""#行驶里程m
    carInfo["dutypaidProof"]= "/upload/1.png" #完税证明

   
    bizParams["carInfo"] = carInfo




	
    financeInfo = {} #金融方案信息
    financeInfo["guidePrice"] = "201000.00" #厂商指导价
    financeInfo["totalCost"] = "216000"  #总成本
    financeInfo["downPaymentsPercent"] = “0.05”  #首付比例
    financeInfo["downPaymentsPayNo"] = "1000000011"   #首付金额
    financeInfo["interestRate"] = "0.08"  #利率
    financeInfo["nameInstalments"] = "11500" #名义月供
    financeInfo["instalmentAmount"] = "11500" #实际月供
    financeInfo["startDate"] = "20180411" #租约开始日
    financeInfo["endDate"] = "20190211"   #租约结束日
    financeInfo["restAmountPercent"] = "0.1" #尾款比例
    financeInfo["restAmount"] = "2222”  #尾款金额-相当于资产方推送过来的残值
    financeInfo["downPaymentsPayType"] = "ALIPAY" #首付支付方式：POS-POS机刷卡，TMALL-天猫，ALIPAY-支付宝
    financeInfo["downPaymentsAmount"] = "20000"#首付金额
    financeInfo["term"] = "12" #租期
    financeInfo["modelFinancialScheme"] = "REFUNDABLE" #选择的该车型金融方案：REFUNDABLE-可退；NON_REFUNDABLE-不可退


    bizParams["financeInfo"] = financeInfo
    
    

    repayPlanList = [] #还款信息
    repayPlanObj1 = {}
    repayPlanObj1["term"] = "1" #代表第几期
    repayPlanObj1["repayDate"] = "20180311" #应还款日
    repayPlanObj1["nameInstalments"] = "11500" #名义月供
    repayPlanObj1["repayAmount"] = "11500"   #应还款金额 
    repayPlanObj1["repayPrincipal"] = "11000"    #应还款本金
    repayPlanObj1["repayInterest"] = "500"    #应还款利息
    repayPlanObj1["status"] = "REPAID" #状态：REPAID-已还款，WAITING-待还款
    repayPlanObj1["factRepayAmount"] = "11500"  #实际还款金额
    repayPlanObj1["factRepayDate"] = "20180311"    #实际还款日期
    repayPlanObj1["penaltyInterest"] = "0"    #罚息，如果没有罚息，则为0
    repayPlanObj1["benefitType"] = "RETURN_CASH"    #优惠方式，DEDUCT-抵扣，RETURN_CASH-返现，抵扣方式时，实际月供 = 名义月供 – 优惠金额，返现方式时，实际月供=名义月供
    repayPlanObj1["benefit"] = "500"    #优惠金额
    repayPlanObj1["payNo"] = "20171109620003785762S"   #支付流水号
    
    repayPlanList.append(repayPlanObj1)

    repayPlanObj2 = {}
    repayPlanObj2["term"] = "2"
    repayPlanObj2["repayDate"] = "20180411"
    repayPlanObj2["nameInstalments"] = "11500"
    repayPlanObj2["repayAmount"] = "11500"    
    repayPlanObj2["repayPrincipal"] = "11000"    
    repayPlanObj2["repayInterest"] = "500"    
    repayPlanObj2["status"] = "WAITING"    
    repayPlanObj2["factRepayAmount"] = "0"  
    repayPlanObj2["factRepayDate"] = "0" 	    
    repayPlanObj2["penaltyInterest"] = "0"    
    repayPlanObj2["benefitType"] = "RETURN_CASH"    
    repayPlanObj2["benefit"] = "500"    
    repayPlanObj2["payNo"] = "20171109620003785762S"
    repayPlanList.append(repayPlanObj2)

    
    repayPlanObj3 = {}
    repayPlanObj3["term"] = "3"
    repayPlanObj3["repayDate"] = "20180511"
    repayPlanObj3["nameInstalments"] = "11500"
    repayPlanObj3["repayAmount"] = "11500"    
    repayPlanObj3["repayPrincipal"] = "11000"    
    repayPlanObj3["repayInterest"] = "500"    
    repayPlanObj3["status"] = "WAITING"    
    repayPlanObj3["factRepayAmount"] = "0"    
    repayPlanObj3["factRepayDate"] = "0"    
    repayPlanObj3["penaltyInterest"] = "0"    
    repayPlanObj3["benefitType"] = "RETURN_CASH"    
    repayPlanObj3["benefit"] = "500"    
    repayPlanObj3["payNo"] = "20171109620003785762S"   
    repayPlanList.append(repayPlanObj3)

    repayPlanObj4 = {}
    repayPlanObj4["term"] = "4"
    repayPlanObj4["repayDate"] = "20180611"
    repayPlanObj4["nameInstalments"] = "11500"
    repayPlanObj4["repayAmount"] = "11500"    
    repayPlanObj4["repayPrincipal"] = "11000"    
    repayPlanObj4["repayInterest"] = "500"    
    repayPlanObj4["status"] = "WAITING"    
    repayPlanObj4["factRepayAmount"] = "0"    
    repayPlanObj4["factRepayDate"] = "0"    
    repayPlanObj4["penaltyInterest"] = "0"    
    repayPlanObj4["benefitType"] = "RETURN_CASH"    
    repayPlanObj4["benefit"] = "500"    
    repayPlanObj4["payNo"] = "20171109620003785762S"   
    repayPlanList.append(repayPlanObj4)


    repayPlanObj5 = {}
    repayPlanObj5["term"] = "5"
    repayPlanObj5["repayDate"] = "20180711"
    repayPlanObj5["nameInstalments"] = "11500"
    repayPlanObj5["repayAmount"] = "11500"    
    repayPlanObj5["repayPrincipal"] = "11000"    
    repayPlanObj5["repayInterest"] = "500"    
    repayPlanObj5["status"] = "WAITING"    
    repayPlanObj5["factRepayAmount"] = "0"    
    repayPlanObj5["factRepayDate"] = "0"    
    repayPlanObj5["penaltyInterest"] = "0"    
    repayPlanObj5["benefitType"] = "RETURN_CASH"    
    repayPlanObj5["benefit"] = "500"    
    repayPlanObj5["payNo"] = "20171109620003785762S"   
    repayPlanList.append(repayPlanObj5)


    repayPlanObj6 = {}
    repayPlanObj6["term"] = "6"
    repayPlanObj6["repayDate"] = "20180811"
    repayPlanObj6["nameInstalments"] = "11500"
    repayPlanObj6["repayAmount"] = "11500"    
    repayPlanObj6["repayPrincipal"] = "11000"    
    repayPlanObj6["repayInterest"] = "500"    
    repayPlanObj6["status"] = "WAITING"    
    repayPlanObj6["factRepayAmount"] = "0"    
    repayPlanObj6["factRepayDate"] = "0"    
    repayPlanObj6["penaltyInterest"] = "0"    
    repayPlanObj6["benefitType"] = "RETURN_CASH"    
    repayPlanObj6["benefit"] = "500"    
    repayPlanObj6["payNo"] = "20171109620003785762S"   
    repayPlanList.append(repayPlanObj6)

    repayPlanObj7 = {}
    repayPlanObj7["term"] = "7"
    repayPlanObj7["repayDate"] = "20180911"
    repayPlanObj7["nameInstalments"] = "11500"
    repayPlanObj7["repayAmount"] = "11500"    
    repayPlanObj7["repayPrincipal"] = "11000"    
    repayPlanObj7["repayInterest"] = "500"    
    repayPlanObj7["status"] = "WAITING"    
    repayPlanObj7["factRepayAmount"] = "0"    
    repayPlanObj7["factRepayDate"] = "0"    
    repayPlanObj7["penaltyInterest"] = "0"    
    repayPlanObj7["benefitType"] = "RETURN_CASH"    
    repayPlanObj7["benefit"] = "500"    
    repayPlanObj7["payNo"] = "20171109620003785762S"   
    repayPlanList.append(repayPlanObj7)



    repayPlanObj8 = {}
    repayPlanObj8["term"] = "8"
    repayPlanObj8["repayDate"] = "20181011"
    repayPlanObj8["nameInstalments"] = "11500"
    repayPlanObj8["repayAmount"] = "11500"    
    repayPlanObj8["repayPrincipal"] = "11000"    
    repayPlanObj8["repayInterest"] = "500"    
    repayPlanObj8["status"] = "WAITING"    
    repayPlanObj8["factRepayAmount"] = "0"    
    repayPlanObj8["factRepayDate"] = "0"    
    repayPlanObj8["penaltyInterest"] = "0"    
    repayPlanObj8["benefitType"] = "RETURN_CASH"    
    repayPlanObj8["benefit"] = "500"    
    repayPlanObj8["payNo"] = "20171109620003785762S"
    repayPlanList.append(repayPlanObj8)


    repayPlanObj9 = {}
    repayPlanObj9["term"] = "9"
    repayPlanObj9["repayDate"] = "20181111"
    repayPlanObj9["nameInstalments"] = "11500"
    repayPlanObj9["repayAmount"] = "11500"    
    repayPlanObj9["repayPrincipal"] = "11000"    
    repayPlanObj9["repayInterest"] = "500"    
    repayPlanObj9["status"] = "WAITING"    
    repayPlanObj9["factRepayAmount"] = "0"    
    repayPlanObj9["factRepayDate"] = "0"    
    repayPlanObj9["penaltyInterest"] = "0"    
    repayPlanObj9["benefitType"] = "RETURN_CASH"    
    repayPlanObj9["benefit"] = "500"    
    repayPlanObj9["payNo"] = "20171109620003785762S"
    repayPlanList.append(repayPlanObj9)

    
    repayPlanObj10 = {}
    repayPlanObj10["term"] = "10"
    repayPlanObj10["repayDate"] = "20181211"
    repayPlanObj10["nameInstalments"] = "11500"
    repayPlanObj10["repayAmount"] = "11500"    
    repayPlanObj10["repayPrincipal"] = "11000"    
    repayPlanObj10["repayInterest"] = "500"    
    repayPlanObj10["status"] = "WAITING"    
    repayPlanObj10["factRepayAmount"] = "0"    
    repayPlanObj10["factRepayDate"] = "0"    
    repayPlanObj10["penaltyInterest"] = "0"    
    repayPlanObj10["benefitType"] = "RETURN_CASH"    
    repayPlanObj10["benefit"] = "500"    
    repayPlanObj10["payNo"] = "20171109620003785762S"   
    repayPlanList.append(repayPlanObj10)

    repayPlanObj11 = {}
    repayPlanObj11["term"] = "11"
    repayPlanObj11["repayDate"] = "20190111"
    repayPlanObj11["nameInstalments"] = "11500"
    repayPlanObj11["repayAmount"] = "11500"    
    repayPlanObj11["repayPrincipal"] = "11000"    
    repayPlanObj11["repayInterest"] = "500"    
    repayPlanObj11["status"] = "WAITING"    
    repayPlanObj11["factRepayAmount"] = "0"    
    repayPlanObj11["factRepayDate"] = "0"    
    repayPlanObj11["penaltyInterest"] = "0"    
    repayPlanObj11["benefitType"] = "RETURN_CASH"    
    repayPlanObj11["benefit"] = "500"    
    repayPlanObj11["payNo"] = "20171109620003785762S"  
    repayPlanList.append(repayPlanObj11)

    repayPlanObj12 = {}
    repayPlanObj12["term"] = "12"
    repayPlanObj12["repayDate"] = "20190211"
    repayPlanObj12["nameInstalments"] = "11500"
    repayPlanObj12["repayAmount"] = "11500"    
    repayPlanObj12["repayPrincipal"] = "11000"    
    repayPlanObj12["repayInterest"] = "500"    
    repayPlanObj12["status"] = "WAITING"    
    repayPlanObj12["factRepayAmount"] = "0"    
    repayPlanObj12["factRepayDate"] = "0"    
    repayPlanObj12["penaltyInterest"] = "0"    
    repayPlanObj12["benefitType"] = "RETURN_CASH"    
    repayPlanObj12["benefit"] = "500"    
    repayPlanObj12["payNo"] = "20171109620003785762S"
    repayPlanList.append(repayPlanObj12)



    bizParams["repayPlan"] = repayPlanList

    bizParams["contractFiles"] = "/upload/20170823/1011/PICKUP20170717190149.pdf"
    bizParams["pickUpFile"] = "/upload/20170823/1011/PICKUP20170717190149.pdf"



    print ("Params-carDasPushAsset: \n"  + json.dumps(bizParams) +  "\n")


carDasPushAssetBizParams()
