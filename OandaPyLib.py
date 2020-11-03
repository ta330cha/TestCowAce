#! /usr/bin/env python

#---PACKAGES---#
import time
import sys
import threading
from datetime import datetime
import os
import requests
import json
import configparser

import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.positions as positions
import oandapyV20.endpoints.transactions as trans

#---Account Info---#
url = os.environ.get('OANDA_API_URL', None)
account_id = os.environ.get('OANDA_API_ACCOUNT_ID', None)
contentType = os.environ.get('OANDA_API_CONTENT_TYPE', None)
authorization = os.environ.get('OANDA_API_AUTHORIZATION', None)
instrument = os.environ.get('OANDA_API_INSTRUMENT', None)

#---APIs---#
api = API(access_token=authorization)
oanda = oandapyV20.API(environment="live",access_token=authorization)

#---NAMES---#
OrderTemplatePathname = './Template/OrderTemplate.json'
TransTemplatePathname = './Template/TransTemplate.json'
OrderRequestsDirName = "./OrderRequests/"

#---Functions---#
def GetPrices():
    params = {"instruments" : instrument}
    req = pricing.PricingInfo(accountID=account_id, params=params)
    res = api.request(req)
    priceTime = res['prices'][0]['time']
    asksPrice = res['prices'][0]['asks'][0]['price']
    bidsPrice = res['prices'][0]['bids'][0]['price']
    return priceTime, asksPrice, bidsPrice

def makeOrder(price, takeProfitPrice, orderType, units):
	pathname = OrderTemplatePathname
	try:
		with open(pathname, "r") as fr:
			params = json.load(fr)
			params["order"]["price"] = str(price)
			params["order"]["takeProfitOnFill"]["price"] = str(takeProfitPrice)
			params["order"]["type"] = orderType
			params["order"]["units"] = units
			return params
	except Exception as e:
		print(e)
	return None

def dumpParam(params):
	dt = datetime.now().strftime('%Y%m%d%H%M%S%f')
	pathname = OrderRequestsDirName + dt + ".json"
	try:
		with open(pathname, "w") as fw:
			json.dump(params, fw)
		return pathname
	except Exception as e:
		print(e)
	return None

def readParam(pathname):
    with open(pathname, "r") as fr:
        params = json.load(fr)
    return params

def BuyLimit(price, takeProfitPrice, units):
	params = makeOrder(price, takeProfitPrice, "LIMIT", units)
	ret = False
	if params is not None:
		dumpParam(params)
		ret = True
	return ret

def BuyStop(price, takeProfitPrice, units):
	params = makeOrder(price, takeProfitPrice, "STOP", units)
	ret = False
	if params is not None:
		dumpParam(params)
		ret = True
	return ret

def SellLimit(price, takeProfitPrice, units):
	params = makeOrder(price, takeProfitPrice, "LIMIT", (-1)*units)
	ret = False
	if params is not None:
		dumpParam(params)
		ret = True
	return ret

def SellStop(price, takeProfitPrice, units):
	params = makeOrder(price, takeProfitPrice, "STOP", (-1)*units)
	ret = False
	if params is not None:
		dumpParam(params)
		ret = True
	return ret

def requestOrderPathname(pathname):
    params = readParam(pathname)
    try:
        req = None
        if params["order"] is not None:
            req = orders.OrderCreate(accountID=account_id, data=params)
        if req is not None:
            res=api.request(req)
            os.remove(pathname)
        return res
    except Exception as e:
        print(e)
    return req

def RequestOrder():
    flag = True
    try:
        files = os.listdir(OrderRequestsDirName)
        if not files:
            flag = False
        if flag == True:
            pathname = OrderRequestsDirName + "/" + files[0]
            requestOrderPathname(pathname)
        return flag
    except Exception as e:
        print(e)
    return flag

#---END---#