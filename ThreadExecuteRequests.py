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

#---Enum---#
class RequestsMode(Enum):
	Default = 0
	Order = 1
	TradeCRCDO = 2

#---Variable---#
RequestsModeFlag = RequestsMode.Default

#---Data Manager---#
class ThreadExecuteRequests():
	def __init__(self, interval, startDelay):
		self.startDelay = startDelay
		self.interval = interval
	
	def task(self, arg, args):
		if RequestsModeFlag == RequestsMode.Order:
			opl.RequestOrder()
			RequestsModeFlag = RequestsMode.TradeCRCDO
		elif RequestsModeFlag == RequestsMode.TradeCRCDO:
			opl.RequestTradeCRCDO()
			RequestsModeFlag = RequestsMode.Default
		else:
			RequestsModeFlag = RequestsMode.Order
	
	def start(self):
		signal.signal(signal.SIGALRM, self.task)
		signal.setitimer(signal.ITIMER_REAL, self.startDelay, self.interval)

#---END---#