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

#---FileName---#
DataFileName = "MarketPrice.csv"

def writeCSV(prices):
	try:
		with open(DataFileName, "a") as fw:
			writer = csv.writer(fw)
			writer.writerow(prices)
		return True
	except Exception as e:
		print(e)
	return False

def readCSV():
	priceList = 0, 0
	try:
		with open(DataFileName, "r") as fr:
			reader = csv.reader(fr, delimiter=',')
			print(reader.Length)
			for line in reader:
				print(line)
	except Exception as e:
		print(e)
	return reader


def setMarketPrice(askPrice, bidPrice):
	table = [askPrice, bidPrice]
	try:
		writeCSV(table)
		return True
	except Exception as e:
		print(e)
	return False

#---END---#