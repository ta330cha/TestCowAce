#! /usr/bin/env python

#---Packages---#
import urllib.parse as pyurllib
import requests as requests
import sys
import datetime
import json
from collections import OrderedDict
import pprint

#---Settings---#
OrderDiff = 0.05
ProfitDiff = 0.5
LimitTIme = 1 #1時間以内の注文を有効とする
BuyLots = 0.05
SellLots = 0.01

#---File Names---#
AccountInfoFile = 'AccountInfo.json'
OrderTemplate = 'OrderTemplate.json'
GetRateTemplate = 'GetRateOrderTemplate.json'

def loadAccountInfo(file):
    with open(file) as f:
        accountInfo = json.load(f)
    url = accountInfo['URL']
    account_id = accountInfo['AccountID']
    modeUrl = url + "/" + "v3/accounts" + "/" + account_id + "/" +"pricing"
    headers = accountInfo['headers'][0]
    return modeUrl, headers

def getRequest(param):
    modeUrl, headers = loadAccountInfo(AccountInfoFile)    
    res = requests.get(modeUrl, headers=headers, params=param)
    print(res)
    return res

def postRequest(param):
    modeUrl, headers = loadAccountInfo(AccountInfoFile)    
    res = requests.post(modeUrl, headers=headers, params=param)
    print(res)
    return res

def buyStop(lots, price, tp):
    with open(OrderTemplate) as f:
        param = json.load(f)
    param["units"] = lots
    param["side"] = "buy"
    param["type"] = "stop"
    param["expiry"] = datetime.datetime.now() + datetime.timedelta(hours=LimitTIme)
    param["price"] = price
    param["lowerBound"] = price - OrderDiff
    param["upperBound"] = price + OrderDiff
    param["takeProfit"] = tp
    postRequest(param)

def sellStop(lots, price, tp):
    with open(OrderTemplate) as f:
        param = json.load(f)
    param["units"] = lots
    param["side"] = "sell"
    param["type"] = "stop"
    param["expiry"] = datetime.datetime.now() + datetime.timedelta(hours=LimitTIme)
    param["price"] = price
    param["lowerBound"] = price - OrderDiff
    param["upperBound"] = price + OrderDiff
    param["takeProfit"] = tp
    postRequest(param)

def buyLimit(lots, price, tp):
    with open(OrderTemplate) as f:
        param = json.load(f)
    param["units"] = lots
    param["side"] = "buy"
    param["type"] = "limit"
    param["expiry"] = datetime.datetime.now() + datetime.timedelta(hours=LimitTIme)
    param["price"] = price
    param["lowerBound"] = price - OrderDiff
    param["upperBound"] = price + OrderDiff
    param["takeProfit"] = tp
    postRequest(param)

def sellLimit(lots, price, tp):
    with open(OrderTemplate) as f:
        param = json.load(f)
    param["units"] = lots
    param["side"] = "sell"
    param["type"] = "limit"
    param["expiry"] = datetime.datetime.now() + datetime.timedelta(hours=LimitTIme)
    param["price"] = price
    param["lowerBound"] = price - OrderDiff
    param["upperBound"] = price + OrderDiff
    param["takeProfit"] = tp
    postRequest(param)

def getPrices():
    with open(GetRateTemplate) as f:
        param = json.load(f)
    res = getRequest(param)
    return res["ask"], res["bid"]

#---END---#