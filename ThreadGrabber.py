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
from OandaApiLib import GetPrices
from OandaJsonLib import DumpPrice

#---Data Manager---#
class ThreadGrabber():
	def __init__(self, interval, startDelay):
		self.startDelay = startDelay
		self.interval = interval
	
	def task(self, arg, args):
		tsGetPrice, ask, bid = GetPrices()
		DumpPrice(tsGetPrice, ask, bid)
	
	def start(self):
		signal.signal(signal.SIGALRM, self.task)
		signal.setitimer(signal.ITIMER_REAL, self.startDelay, self.interval)
		debugWrite = "ThreadGrabber"
		print(debugWrite)

#---END---#