#!/usr/bin/python
# -*- coding: utf-8 -*-
import json



def carDasPushAssetBizParams():

    bizParams = {}
    bizParams["financingNo"] = "HUASHENG-LXX20181026001"
    bizParams["orderNo"] = "DINGDAN-HUASHENG-LXX20181026001"
    bizParams["contractNo"] = "HETONG-HUASHENG-LXX20181026001"
    bizParams["orderFrom"] = "HUASHENG_DIRECT_RENT"
    bizParams["requestDateTime"] = "1502344958000"
    bizParams["pickUpDate"] = "20170812"
    bizParams["bizType"] = "HSHC"
    bizParams["startRepayPlanTerm"] = "2"
    bizParams["endRepayPlanTerm"] = "13"
    
    custInfo = {}
    custInfo["name"] = "_花生"
    custInfo["certType"] = "1"
    custInfo["certNo"] = "110101198010010151"
    custInfo["bankCardNo"] = "6226220001000001"
    custInfo["bankName"] = "CMBC"		
    custInfo["phoneNum"] = "18671345960"
    custInfo["alipayAccount"] = "yang2@wjs.com"
    custInfo["alipayUserId"] = ""#大搜车不为空 花生不校验
    custInfo["certFrontPic"] = ""
    custInfo["certBackPic"] = ""
    custInfo["drivingLicencePic"] = ""
    custInfo["otherCertPics"] = "/upload/20170823/1011/PICKUP20170717190149.pdf"
    bizParams["custInfo"] = custInfo

    gpsInfoList = []
    gpsInfoList1 = {}
    gpsInfoList1["gpsType"] = "SOURCE"
    gpsInfoList1["gpsCode"] = "19120777759"
    gpsInfoList1["gpsOrg"] = "中瑞"
    gpsInfoList.append(gpsInfoList1)

    gpsInfoList2 = {}
    gpsInfoList2["gpsType"] = "NON"
    gpsInfoList2["gpsCode"] = "19120956639"
    gpsInfoList2["gpsOrg"] = "中瑞"
    gpsInfoList.append(gpsInfoList2)

    gpsInfoList3 = {}
    gpsInfoList3["gpsType"] = "NON"
    gpsInfoList3["gpsCode"] = "14142905531"
    gpsInfoList3["gpsOrg"] = "博实结"
    gpsInfoList.append(gpsInfoList3)
    
    carInfo = {}
    carInfo["province"] = "江西"
    carInfo["city"] = "武昌"
    carInfo["carTypeCode"] = "HAFU001"
    carInfo["brandName"] = "长安"
    carInfo["seriesName"] = "悦翔"
    carInfo["modelName"] = "2018款 1.5L DCT豪华型"
    carInfo["year"] = "2018"
    carInfo["vinCode"] = "LSVFS59J532037092"
    carInfo["plateNumber"] = "川LTT155"#"赣C12346"
    carInfo["guidePrice"] = "179000.00"
    carInfo["marketPrice"] = "179000.00"
    carInfo["purchasePrice"] = ""
    carInfo["purchasTax"] = ""
    carInfo["gpsFee"] = ""
    carInfo["licenseFee"] = ""
    carInfo["secondHandHandleFee"] = "300000"
    carInfo["insuranceFee"] = "13"
    carInfo["totalCost"] = "316000"

    insuranceInfoList = []
    insuranceInfo = {}
    insuranceInfo["insuranceType"] = "CAR_BUSINESS"#商业险
    insuranceInfo["insuranceOrgCode"] = "005"
    insuranceInfo["insuranceOrgName"] = "阳光保险"
    insuranceInfo["insuranceNo"] = "805072018630197002787"
    insuranceInfo["insurantCode"] = "91630000MA753MYQXF"
    insuranceInfo["insurantName"] = "水流众生"
    insuranceInfo["insuranceFee"] = "12"
    insuranceInfo["insurancePic"] = "/11rr.jpg"
    insuranceInfo["insuranceOutDate"] = "20180101"
    insuranceInfo["insuranceStartTime"] = "1533551969000"
    insuranceInfo["insuranceEndTime"] = "1565087969000"

    insuranceInfoList.append(insuranceInfo)
    insuranceInfo2 = {}
    insuranceInfo2["insuranceType"] = "CAR_COMPULSORY"  # 交强险
    insuranceInfo2["insuranceOrgCode"] = "005"
    insuranceInfo2["insuranceOrgName"] = "阳光保险"
    insuranceInfo2["insuranceNo"] = "805072018630197002787"
    insuranceInfo2["insurantCode"] = "91630000MA753MYQXF"
    insuranceInfo2["insurantName"] = "水流众生"
    insuranceInfo2["insuranceFee"] = "1"
    insuranceInfo2["insurancePic"] = "/22rr.jpg"
    insuranceInfo2["insuranceOutDate"] = "20180101"
    insuranceInfo2["insuranceStartTime"] = "1533551969000"
    insuranceInfo2["insuranceEndTime"] = "1565087969000"

    insuranceInfoList.append(insuranceInfo2)

    carInfo["insuranceInfo"] = insuranceInfoList
    carInfo["carTax"] = "1"
    carInfo["gpsInfo"] = gpsInfoList
    carInfo["registerCert"] = "111"#花生推送资产信息时，车辆登记证、行驶证要求可以为空
    carInfo["drivingPermitCert"] = "111"#，大搜车推送的，依然要求不能为空。
    carInfo["invoice"] = "156620110001"
   
    bizParams["carInfo"] = carInfo

    bizParams["rentType"] = "DIRECT_RENT"    

    financeInfo = {}
    financeInfo["guidePrice"] = "179000"
    financeInfo["totalCost"] = "316000"
    financeInfo["downPaymentsPercent"] = "0.20"
    financeInfo["downPaymentsPayNo"] = "1000000011"
    financeInfo["downPaymentsPayType"] = "ALIPAY"
    financeInfo["downPaymentsPayNo"] = "20170809500000"
    financeInfo["downPaymentsAmount"]="100000"
    financeInfo["financingPrincipal"] = "96200"#93600-2600=91000
    financeInfo["interestRate"] = "0.08"
    financeInfo["term"] = "13"
    financeInfo["termType"] = "MONTH"
    financeInfo["nameInstalments"] = "2620"
    financeInfo["instalmentAmount"] = "2621"
    financeInfo["startDate"] = "20170930"
    financeInfo["endDate"] = "20191130"
    financeInfo["restAmountPercent"] = "0"
    financeInfo["restAmount"] = "0"	
    financeInfo["leftTerm"] = "12"
    financeInfo["repaidPrincipal"] = "2620"  #用户已还本金 2600*2=5200  23400
    financeInfo["leftPrincipal"] = "72800"  #剩余本金75400-2600=72800   96200
   

    bizParams["financeInfo"] = financeInfo
    
    

    repayPlanList = []
    repayPlanObj1 = {}
    repayPlanObj1["term"] = "1"
    repayPlanObj1["repayDate"] = "20170116"
    repayPlanObj1["nameInstalments"] = "2620"
    repayPlanObj1["repayAmount"] = "2620"    
    repayPlanObj1["repayPrincipal"] = "2600"    
    repayPlanObj1["repayInterest"] = "20"  
    repayPlanObj1["leftPrincipal"] = "91700"  	
    repayPlanObj1["preendAmount"] = "0"  
    repayPlanObj1["status"] = "REPAID" #WAITING      
    repayPlanObj1["totalPenaltyInterest"] = "3"         
    repayPlanList.append(repayPlanObj1)

    
	
    repayPlanObj2 = {}
    repayPlanObj2["term"] = "2"
    repayPlanObj2["repayDate"] = "20170216"
    repayPlanObj2["nameInstalments"] = "2620"
    repayPlanObj2["repayAmount"] = "2620"    
    repayPlanObj2["repayPrincipal"] = "2600"    
    repayPlanObj2["repayInterest"] = "20"  
    repayPlanObj2["leftPrincipal"] = "91700"  	
    repayPlanObj2["preendAmount"] = "0"  
    repayPlanObj2["status"] = "WAITING" #WAITING
    repayPlanObj2["totalPenaltyInterest"] = "2"    
  
    repayPlanList.append(repayPlanObj2)

    repayPlanObj3 = {}
    repayPlanObj3["term"] = "3"
    repayPlanObj3["repayDate"] = "20170316"
    repayPlanObj3["nameInstalments"] = "2620"
    repayPlanObj3["repayAmount"] = "2620"    
    repayPlanObj3["repayPrincipal"] = "2600"    
    repayPlanObj3["repayInterest"] = "20"  
    repayPlanObj3["leftPrincipal"] = "91700"  	
    repayPlanObj3["preendAmount"] = "0"  
    repayPlanObj3["status"] = "WAITING" #WAITING  
    repayPlanObj3["factRepayAmount"] = "0"  #  
    repayPlanObj3["factRepayDate"] = "20170316"    
    repayPlanObj3["penaltyInterest"] = "0"    
    repayPlanObj3["benefitType"] = "RETURN_CASH"    #DEDUCT
    repayPlanObj3["benefit"] = "500"   
    repayPlanObj3["payChannel"] = "ZHONGJIN" 
    repayPlanObj3["payBatchNo"] = "ZHONGJIN" 	
    repayPlanObj3["payNo"] = "201702160300093680000166294"
    
    repayPlanList.append(repayPlanObj3)
    
    repayPlanObj4 = {}
    repayPlanObj4["term"] = "4"
    repayPlanObj4["repayDate"] = "20170416"
    repayPlanObj4["nameInstalments"] = "2620"
    repayPlanObj4["repayAmount"] = "2620"    
    repayPlanObj4["repayPrincipal"] = "2600"    
    repayPlanObj4["repayInterest"] = "20"  
    repayPlanObj4["leftPrincipal"] = "91700"  	
    repayPlanObj4["preendAmount"] = "0"  
    repayPlanObj4["status"] = "WAITING" #WAITING  
    repayPlanObj4["factRepayAmount"] = "0"  #  
    repayPlanObj4["factRepayDate"] = "0"    
    repayPlanObj4["penaltyInterest"] = "0"    
    repayPlanObj4["benefitType"] = "RETURN_CASH"    #DEDUCT
    repayPlanObj4["benefit"] = "500"   
    repayPlanObj4["payChannel"] = "ZHONGJIN" 
    repayPlanObj4["payBatchNo"] = "ZHONGJIN" 	
    repayPlanObj4["payNo"] = "201702160300093680000166294"
    
    repayPlanList.append(repayPlanObj4)

    repayPlanObj5 = {}
    repayPlanObj5["term"] = "5"
    repayPlanObj5["repayDate"] = "20170516"
    repayPlanObj5["nameInstalments"] = "2620"
    repayPlanObj5["repayAmount"] = "2620"    
    repayPlanObj5["repayPrincipal"] = "2600"    
    repayPlanObj5["repayInterest"] = "20"  
    repayPlanObj5["leftPrincipal"] = "91700"  	
    repayPlanObj5["preendAmount"] = "0"  
    repayPlanObj5["status"] = "WAITING" #WAITING  
    repayPlanObj5["factRepayAmount"] = "0"  #  
    repayPlanObj5["factRepayDate"] = ""    
    repayPlanObj5["penaltyInterest"] = "0"    
    repayPlanObj5["benefitType"] = "RETURN_CASH"    #DEDUCT
    repayPlanObj5["benefit"] = "500"   
    repayPlanObj5["payChannel"] = "ZHONGJIN" 
    repayPlanObj5["payBatchNo"] = "ZHONGJIN" 	
    repayPlanObj5["payNo"] = "201702160300093680000166294"
  
    repayPlanList.append(repayPlanObj5)


    repayPlanObj6 = {}
    repayPlanObj6["term"] = "6"
    repayPlanObj6["repayDate"] = "20170616"
    repayPlanObj6["nameInstalments"] = "2620"
    repayPlanObj6["repayAmount"] = "2620"    
    repayPlanObj6["repayPrincipal"] = "2600"    
    repayPlanObj6["repayInterest"] = "20"  
    repayPlanObj6["leftPrincipal"] = "91700"  	
    repayPlanObj6["preendAmount"] = "0"  
    repayPlanObj6["status"] = "WAITING" #WAITING  
    repayPlanObj6["factRepayAmount"] = "0"  #  
    repayPlanObj6["factRepayDate"] = ""    
    repayPlanObj6["penaltyInterest"] = "0"    
    repayPlanObj6["benefitType"] = "RETURN_CASH"    #DEDUCT
    repayPlanObj6["benefit"] = "500"   
    repayPlanObj6["payChannel"] = "ZHONGJIN" 
    repayPlanObj6["payBatchNo"] = "ZHONGJIN" 	
    repayPlanObj6["payNo"] = "201702160300093680000166294"
  
    repayPlanList.append(repayPlanObj6)

    repayPlanObj7 = {}
    repayPlanObj7["term"] = "7"
    repayPlanObj7["repayDate"] = "20170716"
    repayPlanObj7["nameInstalments"] = "2620"
    repayPlanObj7["repayAmount"] = "2620"    
    repayPlanObj7["repayPrincipal"] = "2600"    
    repayPlanObj7["repayInterest"] = "20"  
    repayPlanObj7["leftPrincipal"] = "91700"  	
    repayPlanObj7["preendAmount"] = "0"  
    repayPlanObj7["status"] = "WAITING" #WAITING  
    repayPlanObj7["factRepayAmount"] = "0"  #  
    repayPlanObj7["factRepayDate"] = ""    
    repayPlanObj7["penaltyInterest"] = "0"    
    repayPlanObj7["benefitType"] = "RETURN_CASH"    #DEDUCT
    repayPlanObj7["benefit"] = "500"   
    repayPlanObj7["payChannel"] = "ZHONGJIN" 
    repayPlanObj7["payBatchNo"] = "ZHONGJIN" 	
    repayPlanObj7["payNo"] = "201702160300093680000166294"
  
    repayPlanList.append(repayPlanObj7)

    repayPlanObj8 = {}
    repayPlanObj8["term"] = "8"
    repayPlanObj8["repayDate"] = "20170816"
    repayPlanObj8["nameInstalments"] = "2620"
    repayPlanObj8["repayAmount"] = "2620"    
    repayPlanObj8["repayPrincipal"] = "2600"    
    repayPlanObj8["repayInterest"] = "20"  
    repayPlanObj8["leftPrincipal"] = "91700"  	
    repayPlanObj8["preendAmount"] = "0"  
    repayPlanObj8["status"] = "WAITING" #WAITING  
    repayPlanObj8["factRepayAmount"] = "0"  #  
    repayPlanObj8["factRepayDate"] = ""    
    repayPlanObj8["penaltyInterest"] = "0"    
    repayPlanObj8["benefitType"] = "RETURN_CASH"    #DEDUCT
    repayPlanObj8["benefit"] = "500"   
    repayPlanObj8["payChannel"] = "ZHONGJIN" 
    repayPlanObj8["payBatchNo"] = "ZHONGJIN" 	
    repayPlanObj8["payNo"] = "20160101001"
  
    repayPlanList.append(repayPlanObj8)

    repayPlanObj9 = {}
    repayPlanObj9["term"] = "9"
    repayPlanObj9["repayDate"] = "20170916"
    repayPlanObj9["nameInstalments"] = "2620"
    repayPlanObj9["repayAmount"] = "2620"    
    repayPlanObj9["repayPrincipal"] = "2600"    
    repayPlanObj9["repayInterest"] = "20"  
    repayPlanObj9["leftPrincipal"] = "91700"  	
    repayPlanObj9["preendAmount"] = "0"  
    repayPlanObj9["status"] = "WAITING" #WAITING  
    repayPlanObj9["factRepayAmount"] = "0"  #  
    repayPlanObj9["factRepayDate"] = ""    
    repayPlanObj9["penaltyInterest"] = "0"    
    repayPlanObj9["benefitType"] = "RETURN_CASH"    #DEDUCT
    repayPlanObj9["benefit"] = "500"   
    repayPlanObj9["payChannel"] = "ZHONGJIN" 
    repayPlanObj9["payBatchNo"] = "ZHONGJIN" 	
    repayPlanObj9["payNo"] = "20160101002"
  
    repayPlanList.append(repayPlanObj9)

    repayPlanObj10 = {}
    repayPlanObj10["term"] = "10"
    repayPlanObj10["repayDate"] = "20171016"
    repayPlanObj10["nameInstalments"] = "2620"
    repayPlanObj10["repayAmount"] = "2620"    
    repayPlanObj10["repayPrincipal"] = "2600"    
    repayPlanObj10["repayInterest"] = "20"  
    repayPlanObj10["leftPrincipal"] = "91700"  	
    repayPlanObj10["preendAmount"] = "0"  
    repayPlanObj10["status"] = "WAITING" #WAITING  
    repayPlanObj10["factRepayAmount"] = "0"  #  
    repayPlanObj10["factRepayDate"] = "0"    
    repayPlanObj10["penaltyInterest"] = "0"    
    repayPlanObj10["benefitType"] = "RETURN_CASH"    #DEDUCT
    repayPlanObj10["benefit"] = "500"   
    repayPlanObj10["payChannel"] = "ZHONGJIN" 
    repayPlanObj10["payBatchNo"] = "ZHONGJIN" 	
    repayPlanObj10["payNo"] = "201702160300093680000166294"
  
    repayPlanList.append(repayPlanObj10)

    repayPlanObj11 = {}
    repayPlanObj11["term"] = "11"
    repayPlanObj11["repayDate"] = "20171116"
    repayPlanObj11["nameInstalments"] = "2620"
    repayPlanObj11["repayAmount"] = "2620"    
    repayPlanObj11["repayPrincipal"] = "2600"    
    repayPlanObj11["repayInterest"] = "20"  
    repayPlanObj11["leftPrincipal"] = "91700"  	
    repayPlanObj11["preendAmount"] = "0"  
    repayPlanObj11["status"] = "WAITING" #WAITING  
    repayPlanObj11["factRepayAmount"] = "0"  #  
    repayPlanObj11["factRepayDate"] = "0"    
    repayPlanObj11["penaltyInterest"] = "0"    
    repayPlanObj11["benefitType"] = "RETURN_CASH"    #DEDUCT
    repayPlanObj11["benefit"] = "500"   
    repayPlanObj11["payChannel"] = "ZHONGJIN" 
    repayPlanObj11["payBatchNo"] = "ZHONGJIN" 	
    repayPlanObj11["payNo"] = "201702160300093680000166294"
  
    repayPlanList.append(repayPlanObj11)

    repayPlanObj12 = {}
    repayPlanObj12["term"] = "12"
    repayPlanObj12["repayDate"] = "20171216"
    repayPlanObj12["nameInstalments"] = "2620"
    repayPlanObj12["repayAmount"] = "2620"    
    repayPlanObj12["repayPrincipal"] = "2600"    
    repayPlanObj12["repayInterest"] = "20"  
    repayPlanObj12["leftPrincipal"] = "91700"  	
    repayPlanObj12["preendAmount"] = "0"  
    repayPlanObj12["status"] = "WAITING" #WAITING  
    repayPlanObj12["factRepayAmount"] = "0"  #  
    repayPlanObj12["factRepayDate"] = "0"    
    repayPlanObj12["penaltyInterest"] = "0"    
    repayPlanObj12["benefitType"] = "RETURN_CASH"    #DEDUCT
    repayPlanObj12["benefit"] = "500"   
    repayPlanObj12["payChannel"] = "ZHONGJIN" 
    repayPlanObj12["payBatchNo"] = "ZHONGJIN" 	
    repayPlanObj12["payNo"] = "201702160300093680000166294"
  
    repayPlanList.append(repayPlanObj12)

    repayPlanObj13 = {}
    repayPlanObj13["term"] = "13"
    repayPlanObj13["repayDate"] = "20180116"
    repayPlanObj13["nameInstalments"] = "2620"
    repayPlanObj13["repayAmount"] = "2620"    
    repayPlanObj13["repayPrincipal"] = "2600"    
    repayPlanObj13["repayInterest"] = "20"  
    repayPlanObj13["leftPrincipal"] = "91700"  	
    repayPlanObj13["preendAmount"] = "0"  
    repayPlanObj13["status"] = "WAITING" #WAITING  
    repayPlanObj13["factRepayAmount"] = "0"  #  
    repayPlanObj13["factRepayDate"] = "0"    
    repayPlanObj13["penaltyInterest"] = "0"    
    repayPlanObj13["benefitType"] = "RETURN_CASH"    #DEDUCT
    repayPlanObj13["benefit"] = "500"   
    repayPlanObj13["payChannel"] = "ZHONGJIN" 
    repayPlanObj13["payBatchNo"] = "ZHONGJIN" 	
    repayPlanObj13["payNo"] = "201702160300093680000166294"
  
    repayPlanList.append(repayPlanObj13)


	
    bizParams["repayPlan"] = repayPlanList
	
    factRepayList = []
    factRepayObj1 = {}
    factRepayObj1["term"] = "1"  
    factRepayObj1["factRepayAmount"] = "1722"  #  
    factRepayObj1["factRepayDate"] = "20170127"    
    factRepayObj1["penaltyInterest"] = "2"    
    factRepayObj1["benefitType"] = "RETURN_CASH"    #DEDUCT
    factRepayObj1["benefit"] = "500"   
    factRepayObj1["payChannel"] = "ZHONGJIN" 
    factRepayObj1["payBatchNo"] = "2017021603001" 	
    factRepayObj1["payNo"] = "13800000001"
    factRepayObj1["repayNo"] = "11"
    
    factRepayList.append(factRepayObj1)



    factRepayObj2 = {}
    factRepayObj2["term"] = "1"
    factRepayObj2["factRepayAmount"] = "901"  #  实际还款金额=月供+罚息
    factRepayObj2["factRepayDate"] = "20170126"
    factRepayObj2["penaltyInterest"] = "1"
    factRepayObj2["benefitType"] = "RETURN_CASH"    #DEDUCT
    factRepayObj2["benefit"] = "500"
    factRepayObj2["payChannel"] = "ZHONGJIN"
    factRepayObj2["payBatchNo"] = "20170216030002"
    factRepayObj2["payNo"] = "201702160300093680000166294"
    factRepayObj2["repayNo"] = "12"
    factRepayList.append(factRepayObj2)
	
	

  

    bizParams["factRepay"] = factRepayList

    bizParams["contractFiles"] = "/upload/20170823/1011/PICKUP20170717190149.pdf"
    bizParams["pickUpFile"] = "/upload/20170823/1011/PICKUP20170717190149.pdf"
    bizParams["otherContractFiles"] = ""



    print ("Params-carDasPushAsset: \n"  + json.dumps(bizParams) +  "\n")


carDasPushAssetBizParams()
