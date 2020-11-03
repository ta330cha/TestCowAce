#! /usr/bin/env python
# -*- coding: utf-8 -*-

#---Packages---#
import pandas as pd
import datetime
from datetime import datetime,timedelta
import time
import json
import csv

#---DB Settings---#
Address = "150.95.130.99.8080"
DataBaseName = "cowaceDB"
HostName = "script"
PassWord = "cowace"

#---Table Names---#
TimeStampTable = "TS"
PredictDataTable = "PredictResult"
MarketDataTable = "MarketResult"

class ArpCSVList():
    def __init__(self):
        self.filename = "MarketPrice.csv"

    def __del__(self):
        #Logout from DB
        print("Destruct ArpOandaPy")
    
    def writeCSV(self, prices):
        try:
            with open(self.filename, "a") as fw:
                writer = csv.writer(fw)
                writer.writerow(prices)
            return True
        except Exception as e:
            print(e)
        return False
    
    def getTimeStamp(self):
        tableName = TimeStampTable
        return datetime.now()
    
    def setMarketPrice(self, askPrice, bidPrice):
        table = [askPrice, bidPrice]
        try:
            self.writeCSV(table)
            return True
        except Exception as e:
            print(e)
        return False
    
#---END---#