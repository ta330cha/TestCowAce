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
from OandaApiLib import RequestOrder
from OandaApiLib import RequestTradeCRCDO

#---Enum---#
class RequestsMode(Enum):
	Default = 0
	Order = 1
	TradeCRCDO = 2

#---Data Manager---#
class ThreadExecuteRequests():
	def __init__(self, interval, startDelay):
		self.startDelay = startDelay
		self.interval = interval
		self.requestsModeFlag = RequestsMode.Default
	
	def task(self, arg, args):
		if RequestsModeFlag == RequestsMode.Order:
			RequestOrder()
			self.requestsModeFlag = RequestsMode.TradeCRCDO
		elif RequestsModeFlag == RequestsMode.TradeCRCDO:
			RequestTradeCRCDO()
			self.requestsModeFlag = RequestsMode.Default
		else:
			self.requestsModeFlag = RequestsMode.Order
	
	def start(self):
		signal.signal(signal.SIGALRM, self.task)
		signal.setitimer(signal.ITIMER_REAL, self.startDelay, self.interval)
		debugWrite = "Start ThreadExecuteRequests"
		print(debugWrite)

#---END---#