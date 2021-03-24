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

import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.positions as positions
import oandapyV20.endpoints.transactions as trans
import oandapyV20.endpoints.trades as trades

#---Library---#
import DebugLib as debug
import Config as config
from OandaJsonLib import ReadParam
from OandaJsonLib import GetFileList

#---Account Info---#
url = config.get("OANDA_API_URL")
account_id = config.get("OANDA_API_ACCOUNT_ID")
contentType = config.get("OANDA_API_CONTENT_TYPE")
authorization = config.get("OANDA_API_AUTHORIZATION")
instrument = config.get("OANDA_API_INSTRUMENT")

#---NAMES---#
OrderTemplatePathname = PathnameConfig.Get("OrderTemplatePathname")
TransTemplatePathname = PathnameConfig.Get("TransTemplatePathname")
TradeTemplatePathname = PathnameConfig.Get("TradeTemplatePathname")
PriceTemplatePathname = PathnameConfig.Get("PriceTemplatePathname")
OrderRequestsDirName = PathnameConfig.Get("OrderRequestsDirName")
TransRequestsDirName = PathnameConfig.Get("TransRequestsDirName")
TradeRequestsDirName = PathnameConfig.Get("TradeRequestsDirName")
PriceDirName = PathnameConfig.Get("PriceDirName")

#---Settings---#
MarginLevelLimit = 48

#---APIs---#
api = API(access_token=authorization)
oanda = oandapyV20.API(environment="live",access_token=authorization)

#---Functions---#
def GetMarginLevel():
	ret = 0
	try:
		req = accounts.AccountSummary(accountID=account_id)
		res = api.request(req)
		marginAvailable = float(res["account"]["marginAvailable"])
		marginUsed = float(res["account"]["marginUsed"])
		ret = 50 * marginUsed / marginAvailable
	except Exception as e:
		print(e)
	return ret

def GetPrices():
	params = {"instruments" : instrument}
	priceTime = None
	asksPrice = None
	bidsPrice = None
	try:
		req = pricing.PricingInfo(accountID=account_id, params=params)
		res = api.request(req)
		priceTime = res['prices'][0]['time']
		asksPrice = res['prices'][0]['asks'][0]['price']
		bidsPrice = res['prices'][0]['bids'][0]['price']
	except Exception as e:
		print(e)
	return instrument, priceTime, asksPrice, bidsPrice

def requestOrderPathname(pathname):
	params = ReadParam(pathname)
	res = None
	try:
		req = orders.OrderCreate(accountID=account_id, data=params)
		if req is not None:
			res=api.request(req)
			os.remove(pathname)
		return res
	except Exception as e:
		print(e)
	return res

def requestTradeCRCDOPathname(pathname):
	rParams = ReadParam(pathname)
	tradeId = rParams["tradeID"]
	params = rParams["trades"]
	res = None
	try:
		req = trades.TradeCRCDO(accountID=account_id, tradeID=tradeId, data=params)
		if req is not None:
			res=api.request(req)
			os.remove(pathname)
		return res
	except Exception as e:
		print(e)
	return res

def RequestOrder():
	flag = True
	try:
		files = GetFileList(OrderRequestsDirName)
		if not files:
			flag = False
		if flag == True:
			pathname = OrderRequestsDirName + "/" + files[0]
			res = requestOrderPathname(pathname)
			print(res)
			debug.printDebug1(res, "RequestOrder")
			print(res)
		return flag
	except Exception as e:
		print(e)
	return flag

def RequestTradeCRCDO():
	flag = True
	try:
		files = GetFileList(TradeRequestsDirName)
		if not files:
			flag = False
		if flag == True:
			pathname = TradeRequestsDirName + "/" + files[0]
			res = requestTradeCRCDOPathname(pathname)
			debug.printDebug1(res, "RequestTradeCRCDO")
			print(res)
		return flag
	except Exception as e:
		print(e)
	return flag

def GetPositonPrice(tradeId):
	ret = 0
	try:
		req = trans.TransactionDetails(accountID=account_id, transactionID=tradeId)
		res = api.request(req)
		ret = float(res['transaction']['price'])
	except Exception as e:
		print(e)
	return ret

def GetPositionList():
	try:
		req = positions.PositionList(accountID=account_id)
		res = api.request(req)
	except Exception as e:
		print(e)
	return res

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

#---END---#