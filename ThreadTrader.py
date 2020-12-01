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
import OandaPyLib as opl
import MovingAverage as ma
import DecisionTrend as dect
import FibonacciRetracement as fibo

#---Setting---#
LimitDiffPrice = 0.05
TradeLot = 10

#---Local Var---#
class ThreadTrader():
	def __init__(self, interval, startDelay):
		self.startDelay = startDelay
		self.interval = interval
	
	def taskSetPosition(self, askList, bidList, askNow, bidNow):
		print("---SetPosition---")

	def taskTrade(self, askList, bidList, askNow, bidNow):
		askData = np.array(askList)
		bidData = np.array(bidList)
		trendFlag = dect.EstDecisionTrend(askData, bidData)
		fibMax, fibMin = fibo.EstFibonacciRetracement(askData, bidData)
		print("AsKNow = {0}, BidNow = {1}, Trend = {2}, FibonacciMax = {3}, FibonacciMin = {4}".format(askNow, bidNow, trendFlag, fibMax, fibMin))
		if trendFlag > 0 and fibMax - bidNow > LimitDiffPrice:
			opl.BuyStop(bidNow+LimitDiffPrice, fibMax, TradeLot)
		elif trendFlag < 0 and askNow - fibMin > LimitDiffPrice:
			opl.SellStop(askNow-LimitDiffPrice, fibMin, TradeLot)
		else:
			print("No Order")
		

	def task(self, arg, args):
		askList, bidList, count = opl.GetJsonPricesList()
		print("Data Count = {}".format(count))
		askNow, bidNow = askList[-1], bidList[-1]
		self.taskSetPosition(askList, bidList, askNow, bidNow)
		if opl.GetMarginLevel() < opl.MarginLevelLimit:
			self.taskTrade(askList, bidList, askNow, bidNow)
		else:
			print("Margin Limit Over!!")
	
	def start(self):
		signal.signal(signal.SIGALRM, self.task)
		signal.setitimer(signal.ITIMER_REAL, self.startDelay, self.interval)

#---END---