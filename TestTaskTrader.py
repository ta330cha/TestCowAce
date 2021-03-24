#! /usr/bin/env python

#---Packages---#
import urllib.parse as pyurllib
import requests as requests
import sys
import os
import datetime
import time
import json
from collections import OrderedDict
import pprint
import numpy as np
import csv

#---Library---#
import OandaJsonLib as ojl
import DecisionTrend as dect

#---Settings---#
TESTDATAFILE = 'MarketPrice.csv'
LimitDiffPrice = 0.06
StoplossDiffPrice = 0.08
TakeProfitDiffPrice = 0.12
TradeLot = 10

#---Config---#
instrument = "USD_JPY"

#---Script---#

#ファイル読み込み
with open (TESTDATAFILE) as csvfile:
	sr = csv.reader(csvfile, delimiter=',', quotechar=',')
	for row in sr:
		dtNow = datetime.datetime.now()
		ask = row[0]
		bid = row[1]
		ojl.DumpPrice(instrument, dtNow, ask, bid)

askList, bidList, count = ojl.GetPricesJsonList()

print("Data Count = {}".format(count))

if count > 0:
	askNow, bidNow = askList[-1], bidList[-1]
	askData = np.array(askList)
	bidData = np.array(bidList)
	trendFlag = dect.EstDecisionTrend(askData, bidData)
	if trendFlag > 0.05:
		tradePrice = bidNow+LimitDiffPrice
		tradeTakeProfit = tradePrice + TakeProfitDiffPrice
		tradeStojlossPrice = tradePrice - StoplossDiffPrice
		ojl.BuyStop(tradePrice, tradeTakeProfit, tradeStojlossPrice, TradeLot)
		debugWrite = f'Order at {tradePrice} as Buy'
		print(debugWrite)
	elif trendFlag < -0.05:
		tradePrice = askNow+LimitDiffPrice
		tradeTakeProfit = tradePrice - TakeProfitDiffPrice
		tradeStojlossPrice = tradePrice + StoplossDiffPrice
		ojl.SellStop(tradePrice, tradeTakeProfit, tradeStojlossPrice, TradeLot)
		debugWrite = f'Order at {tradePrice} as Sell'
		print(debugWrite)
	else:
		print("No Order")

#---END---#