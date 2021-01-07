#! /usr/bin/env python

#---Packages---#
import urllib.parse as pyurllib
import requests as requests
import sys
import os
import datetime
import json
from collections import OrderedDict
import pprint
import numpy as np

from oandapyV20 import API
from oandapyV20.endpoints.trades import TradeCRCDO, TradeDetails
import oandapyV20.endpoints.positions as positions
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.transactions as trans

#---My Package---#
import OandaPyLib as opl

#---Account Info---#
url = os.environ.get('OANDA_API_URL', None)
account_id = os.environ.get('OANDA_API_ACCOUNT_ID', None)
contentType = os.environ.get('OANDA_API_CONTENT_TYPE', None)
authorization = os.environ.get('OANDA_API_AUTHORIZATION', None)
instrument = os.environ.get('OANDA_API_INSTRUMENT', None)

#---Manager---#

#---API---#
api = API(access_token=authorization)
#oanda = oandapyV20.API(environment="live",access_token=authorization)

#---Start Script---#
ACC_NUMBER = account_id
r=positions.PositionList(accountID=ACC_NUMBER)###EEE
response=api.request(r)###EEE
print(response)
tradeBuyList = response['positions'][0]['long']['tradeIDs']
print(tradeBuyList)
r=trans.TransactionDetails(accountID=ACC_NUMBER, transactionID=tradeBuyList[0])
response=api.request(r)###EEE
print(response)

#tradeSellList = response['positions'][0]['short']['tradeIDs']
#print(tradeSellList)

#---End---#