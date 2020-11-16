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

#---My Package---#
import OandaPyLib as opl
from ArpCSVList import ArpCSVList

#---Account Info---#
url = os.environ.get('OANDA_API_URL', None)
account_id = os.environ.get('OANDA_API_ACCOUNT_ID', None)
contentType = os.environ.get('OANDA_API_CONTENT_TYPE', None)
authorization = os.environ.get('OANDA_API_AUTHORIZATION', None)
instrument = os.environ.get('OANDA_API_INSTRUMENT', None)

#---Manager---#
dataMng = ArpCSVList()


#---Start Script---#
api = API(access_token=authorization)

data01={
    "stopLoss": {
        "price": "101.000",
        "timeInForce": "GTC",
    },
}

print(data01)

trade_id = 217
ep=TradeCRCDO(accountID=account_id,tradeID=trade_id,data=data01)
rsp=api.request(ep)

#---End---#