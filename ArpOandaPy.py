#! /usr/bin/env python
# -*- coding: utf-8 -*-

#---Packages---#
import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.positions as positions
import pandas as pd
import datetime
from datetime import datetime,timedelta
import pytz
import configparser
import time
import json
from collections import OrderedDict
import pprint

#---Settings---#
OrderDiff = 0.05
TakeProfitDiff = 0.5
LimitTime = 1 #1時間以内の注文を有効とする
BuyLots = 0.05
SellLots = 0.01

#---File Names---#
AccountInfoFile = 'AccountInfo.json'
OrderTemplate = 'OrderTemplate.json'

class ArpOandaPy():
    def __init__(self, filenameAccountInfo):
        with open(filenameAccountInfo) as fAccountInfo:
            accountInfo = json.load(fAccountInfo)
        self.AccountID = accountInfo['AccountID']
        self.AccountNum = accountInfo['AccountNum']
        self.UserToken = accountInfo['user_token']
        self.Api = oandapyV20.API(access_token=self.UserToken)
    
    def __del__(self):
        #Logout from DB
        print("Destruct ArpOandaPy")
    
    def GetPrice(self):
        ask = 180
        bid = 170
        return ask, bid
    
    def GetAccountInfo(self):
        barance = 3000000
        margineLevel = 200000
        return barance, margineLevel
    
    def GetOrdersList(self):
        orderList = []
        return orderList
    
    def GetOrderPrice(self, ticket):
        price = 170
        return price
    
    def ChangeOrder(self, ticket, tp):
        return True
    
    def DeleteOrder(self, ticket):
        return False
    
    def GetPositionsList(self):
        positionList = []
        return positionList
    
    def GetPositon(self, ticket):
        lot = 1.0 # Lot
        positionPrice = 106.500 # Price when got position
        price = 106.000 # Price at now
        tp = 107.000 # Takeprofit settled
        sl = 105.000 # Stoploss settled
        return lot, positionPrice, price, tp, sl
    
    def ChangePosition(self, ticket, tp):
        return True

    def BookBuy(self, lots, price, tp):
        with open(OrderTemplate) as f:
            param = json.load(f)
        param["order"]["price"] = price
        param["order"]["takeProfitOnFill"]["price"] = tp
        param["units"] = lots
        r = orders.OrderCreate(self.AccountID, data=param)
        res = self.Api.request(r)
        return res
    
    def BookSell(self, lots, price, tp):
        with open(OrderTemplate) as f:
            param = json.load(f)
        param["order"]["price"] = price
        param["order"]["takeProfitOnFill"]["price"] = tp
        param["units"] = lots * (-1)
        r = orders.OrderCreate(self.AccountID, data=param)
        res = self.Api.request(r)
        return res
    
#---END---#