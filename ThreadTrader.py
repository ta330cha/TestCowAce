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

class ThreadTrader():
	def __init__(self, interval, startDelay):
		self.startDelay = startDelay
		self.interval = interval
	
	def taskSetPosition(self):
		print("---SetPosition---")

	def taskTrade(self):
		askList, bidList, count = opl.GetJsonPricesList()
		askNow, bidNow = askList[-1], bidList[-1]
		askData = np.array(askList)
		bidData = np.array(bidList)
		trendFlag = dect.EstDecisionTrend(askData, bidData)
		fibMax, fibMin = fibo.EstFibonacciRetracement(askData, bidData)
		print("Trend = {0}, FibonacciMax = {1}, FibonacciMin = {2}".format(trendFlag, fibMax, fibMin))
		if trendFlag > 0 and fibMax - bidNow > LimitDiffPrice:
			opl.BuyStop(bidNow+LimitDiffPrice, fibMax, TradeLot)
		elif trendFlag < 0 and askNow - fibMin > LimitDiffPrice:
			opl.SellStop(askNow-LimitDiffPrice, fibMin, TradeLot)
		else:
			print("Trend = {0}, FibonacciMax = {1}, FibonacciMin = {2}".format(trendFlag, fibMax, fibMin))

	def task(self, arg, args):
		self.taskSetPosition()
		self.taskTrade()
	
	def start(self):
		signal.signal(signal.SIGALRM, self.task)
		signal.setitimer(signal.ITIMER_REAL, self.startDelay, self.interval)

#---END---