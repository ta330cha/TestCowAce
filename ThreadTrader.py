##!/usr/bin/env python
# -*- coding: utf-8 -*-

#---Packages---#
import socket
import threading
import time
from datetime import datetime
from enum import Enum
import signal
import numpy as np

#---Library---#
import OandaJsonLib as ojl
import DecisionTrend as dect

#---Setting---#
LimitDiffPrice = 0.06
StoplossDiffPrice = 0.08
TakeProfitDiffPrice = 0.12
TradeLot = 10

#---Local Var---#
class ThreadTrader():
	def __init__(self, interval, startDelay):
		self.startDelay = startDelay
		self.interval = interval
	
	def taskSetPosition(self, askList, bidList, askNow, bidNow):
		buyPositionList, sellPositionList  = ojl.GetPositionLists()
		ojl.AdjustmentBuyPosition(buyPositionList, askNow, bidNow, LimitDiffPrice)
		ojl.AdjustmentSellPosition(sellPositionList, askNow, bidNow, LimitDiffPrice)

	def taskIncreaseTrend(self):
		tradePrice = bidNow+LimitDiffPrice
		tradeTakeProfit = tradePrice + TakeProfitDiffPrice
		tradeStojlossPrice = tradePrice - StoplossDiffPrice
		ojl.BuyStop(tradePrice, tradeTakeProfit, tradeStojlossPrice, TradeLot)
		debugWrite = f'Order at {tradePrice} as Buy'
		print(debugWrite)
	
	def taskDecreaseTrend(self):
		tradePrice = askNow+LimitDiffPrice
		tradeTakeProfit = tradePrice - TakeProfitDiffPrice
		tradeStojlossPrice = tradePrice + StoplossDiffPrice
		ojl.SellStop(tradePrice, tradeTakeProfit, tradeStojlossPrice, TradeLot)
		debugWrite = f'Order at {tradePrice} as Sell'
		print(debugWrite)

	def taskTrade(self, askList, bidList, askNow, bidNow):
		askData = np.array(askList)
		bidData = np.array(bidList)
		trendFlag = dect.EstDecisionTrend(askData, bidData)
		if trendFlag > 0.05:
			self.taskIncreaseTrend()
		elif trendFlag < -0.05:
			self.taskDecreaseTrend()
		else:
			print("No Order")
	
	def task(self, arg, args):
		askList, bidList, count = ojl.GetPricesJsonList()
		print("Data Count = {}".format(count))
		if count > 0:
			askNow, bidNow = askList[-1], bidList[-1]
			self.taskSetPosition(askList, bidList, askNow, bidNow)
			self.taskTrade(askList, bidList, askNow, bidNow)
	
	def start(self):
		signal.signal(signal.SIGALRM, self.task)
		signal.setitimer(signal.ITIMER_REAL, self.startDelay, self.interval)
		debugWrite = "Start ThreadTrader"
		print(debugWrite)

#---END---