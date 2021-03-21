#! /usr/bin/env python

#---PACKAGES---#
import time
import sys
import threading
from datetime import datetime
import os
from types import resolve_bases
import requests
import json

#---Library---#
import DebugLib as debug
import Config

#---Config---#
PathnameConfig = Config.Config('./Configs/Pathname.json')

#---NAMES---#
OrderTemplatePathname = PathnameConfig.Get("OrderTemplatePathname")
TransTemplatePathname = PathnameConfig.Get("TransTemplatePathname")
TradeTemplatePathname = PathnameConfig.Get("TradeTemplatePathname")
PriceTemplatePathname = PathnameConfig.Get("PriceTemplatePathname")
OrderRequestsDirName = PathnameConfig.Get("OrderRequestsDirName")
TransRequestsDirName = PathnameConfig.Get("TransRequestsDirName")
TradeRequestsDirName = PathnameConfig.Get("TradeRequestsDirName")
PriceDirName = PathnameConfig.Get("PriceDirName")

#---Functions---#
def GetFileList(dirName):
	ret = None
	try:
		temp = os.listdir(dirName)
		ret = sorted(temp)
	except Exception as e:
		print(e)
	return ret

def GetPricesJson():
	ask = 0
	bid = 0
	try:
		files = GetFileList(PriceDirName)
		flag = True
		if not files:
			flag = False
		if flag == True:
			pathname = PriceDirName + "/" + files[0]
			ask, bid = GetPricesJsonPathname(pathname)
	except Exception as e:
		print(e)
	return ask, bid

def GetPricesJsonPathname(pathname):
	ask = 0
	bid = 0
	try:
		params = ReadParam(pathname)
		ask = float(params["asks"])
		bid = float(params["bids"])
		os.remove(pathname)	
	except Exception as e:
		print(e)
	return ask, bid

def GetPricesJsonList():
	count = 0
	askList = []
	bidList = []
	try:
		files = GetFileList(PriceDirName)
		flag = True
		if not files:
			flag = False
		while flag == True:
			count = count + 1
			pathname = PriceDirName + "/" + files[0]
			ask, bid = GetPricesJsonPathname(pathname)
			askList.append(ask)
			bidList.append(bid)
			files = os.listdir(PriceDirName)
			if not files:
				flag = False
			else:
				flag = True
	except Exception as e:
		print(e)
	return askList, bidList, count

def makeOrder(price, takeProfitPrice, stopLossPrice, orderType, units):
	pathname = OrderTemplatePathname
	try:
		with open(pathname, "r") as fr:
			params = json.load(fr)
			params["order"]["price"] = str(price)
			params["order"]["takeProfitOnFill"]["price"] = str(takeProfitPrice)
			params["order"]["stopLossOnFill"]["price"] = str(stopLossPrice)
			params["order"]["type"] = orderType
			params["order"]["units"] = units
			return params
	except Exception as e:
		print(e)
	return None

def makeStopLoss(tradeId, stopLossPrice):
	pathname = TradeTemplatePathname
	try:
		with open(pathname, "r") as fr:
			params = json.load(fr)
			params["tradeID"] = tradeId
			params["trades"]["stopLoss"]["price"] = str(stopLossPrice)
			return params
	except Exception as e:
		print(e)

def dumpParam(params, dirName):
	dt = datetime.now().strftime('%Y%m%d%H%M%S%f')
	pathname = dirName + dt + ".json"
	try:
		with open(pathname, "w") as fw:
			json.dump(params, fw)
	except Exception as e:
		print(e)
		return None
	return pathname

def dumpOrderParam(params):
	dirName = OrderRequestsDirName
	return dumpParam(params, dirName)

def dumpPriceParam(params):
	dirName = PriceDirName
	return dumpParam(params, dirName)

def dumpTradeParam(params):
	dirName = TradeRequestsDirName
	return dumpParam(params, dirName)

def ReadParam(pathname):
	with open(pathname, "r") as fr:
		params = json.load(fr)
	return params

def BuyLimit(price, takeProfitPrice, stopLossPrice, units):
	params = makeOrder(price, takeProfitPrice, stopLossPrice , "LIMIT", units)
	ret = False
	if params is not None:
		dumpOrderParam(params)
		ret = True
	return ret

def BuyStop(price, takeProfitPrice, stopLossPrice, units):
	params = makeOrder(price, takeProfitPrice, stopLossPrice, "STOP", units)
	ret = False
	if params is not None:
		dumpOrderParam(params)
		ret = True
	return ret

def SellLimit(price, takeProfitPrice, stopLossPrice, units):
	params = makeOrder(price, takeProfitPrice, stopLossPrice, "LIMIT", (-1)*units)
	ret = False
	if params is not None:
		dumpOrderParam(params)
		ret = True
	return ret

def SellStop(price, takeProfitPrice, stopLossPrice, units):
	params = makeOrder(price, takeProfitPrice, stopLossPrice, "STOP", (-1)*units)
	ret = False
	if params is not None:
		dumpOrderParam(params)
		ret = True
	return ret

def SetStopLoss(tradeId, stopLossPrice):
	params = makeStopLoss(tradeId, stopLossPrice)
	ret = False
	if params is not None:
		dumpTradeParam(params)
		ret = True
	return ret

def DumpPrice(timeGetPrice, asksPrice, bidsPrice):
	pathname = None
	rParams = ReadParam(PriceTemplatePathname)
	try:
		rParams["instruments"] = str(instrument)
		rParams["time"] = str(timeGetPrice)
		rParams["asks"] = str(asksPrice)
		rParams["bids"] = str(bidsPrice)
		dumpPriceParam(rParams)
	except Exception as e:
		print(e)
	return pathname

def GetPositionList():
	try:
		req = positions.PositionList(accountID=account_id)
		res = api.request(req)
	except Exception as e:
		print(e)
	return res

def GetBuyPositionList(positionList):
	return positionList['positions'][0]['long']['tradeIDs']

def GetSellPositionList(positionList):
	return positionList['positions'][0]['short']['tradeIDs']

def GetPositionLists():
	buyPositionList = None
	sellPositionList = None
	try:
		positionList = GetPositionList()
		buyPositionList = GetBuyPositionList(positionList)
		sellPositionList = GetSellPositionList(positionList)
	except Exception as e:
		print(e)
	return buyPositionList, sellPositionList

def AdjustmentBuyPosition(positionList, askNow, bidNow, limitDiffPrice):
	ret = False
	if positionList is None:
		return ret
	try:
		print("Set StopLoss {0}".format(len(positionList)))
		for tradeId in positionList:
			if GetPositonPrice(tradeId) < askNow - limitDiffPrice:
				stopLossPrice = askNow - limitDiffPrice
				SetStopLoss(tradeId, stopLossPrice)
				ret = True
				print("Set StopLoss as {0} for {1}".format(stopLossPrice, tradeId))
			else:
				print("Did not Set StopLoss for {0}".format(tradeId))
	except Exception as e:
		print(e)
	return ret

def AdjustmentSellPosition(positionList, askNow, bidNow, limitDiffPrice):
	ret = False
	if positionList is None:
		return ret
	try:
		for tradeId in positionList:
			if GetPositonPrice(tradeId) > bidNow - limitDiffPrice:
				stopLossPrice = bidNow + limitDiffPrice
				SetStopLoss(tradeId, stopLossPrice)
				ret = True
				print("Set StopLoss as {0} for {1}".format(stopLossPrice, tradeId))
			else:
				ret = False
				print("Did not Set StopLoss for {0}".format(tradeId))
	except Exception as e:
		print(e)
	return ret

#---END---#