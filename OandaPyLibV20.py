#! /usr/bin/env python

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
ProfitDiff = 0.5
LimitTIme = 1 #1時間以内の注文を有効とする
BuyLots = 0.05
SellLots = 0.01

#---File Names---#
AccountInfoFile = 'AccountInfo.json'
OrderTemplate = 'OrderTemplate.json'

def loadAccountInfo(file):
    

def getRequest(param):



def postRequest(param):
