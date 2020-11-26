#! /usr/bin/env python
# -*- coding: utf-8 -*-

#---Packages---#
import pandas as pd
import datetime
from datetime import datetime,timedelta
import time
import json
from collections import OrderedDict

#---DB Settings---#
Address = "150.95.130.99.8080"
DataBaseName = "cowaceDB"
HostName = "script"
PassWord = "cowace"

#---Table Names---#
TimeStampTable = "TS"
PredictDataTable = "PredictResult"
MarketDataTable = "MarketResult"


class ArpOandaPy():
    def __init__(self):
        self.address = Address
        self.dbName = DataBaseName
        self.hostName = HostName
        self.passWord = PassWord

    def __del__(self):
        #Logout from DB
    
    def getTimeStamp(self):
        tableName = TimeStampTable
        return datetime.now()
    
    def setTimeStamp(self, time):
        tableName = TimeStampTable
        return True
    
    def getData(self, tableName):
        data = []
        return data
    
    def setData(self, tableName, data):
        return True
    
    def getPredictPriceList(self):
        tableName = PredictDataTable
        predictData = self.getData(tableName)
        return predictData
    
    def setPredictPriceList(self, data):
        tableName = PredictDataTable
        ret = self.setData(tableName, data)
        return ret
    
    def getMarketPriceList(self):
        tableName = MarketDataTable
        marketData = self.getData(tableName)
        return marketData
    
    def setPredictPriceList(self, data):
        tableName = MarketDataTable
        ret = self.setData(tableName, data)
        return ret
    
#---END---#