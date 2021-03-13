##!/usr/bin/env python
# -*- coding: utf-8 -*-

#---Packages---#
import socket
import threading
import time
from datetime import datetime
from enum import Enum
import signal

#---Library---#
import OandaPyLib as opl
import ArpCSVList as dataMng
import MovingAverage as ma

#---Data Manager---#
class ThreadSetData():
	def __init__(self, interval, startDelay):
		self.startDelay = startDelay
		self.interval = interval
	
	def task(self, arg, args):
		try:
			ask, bid = opl.GetPricesJson()
			flag = False
			if ask > 0 and bid > 0:
				flag = True
			if flag == True:
				dataMng.SetMarketPrice(ask, bid)
		except Exception as e:
			print(e)
	
	def start(self):
		signal.signal(signal.SIGALRM, self.task)
		signal.setitimer(signal.ITIMER_REAL, self.startDelay, self.interval)

#---END---#