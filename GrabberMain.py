#! /usr/bin/env python
# -*- coding: utf-8 -*-

#---Packages---#
import socket
import time
import sys
import os
import threading
import json
from datetime import datetime
import OandaPyLib as opl
import ArpCSVList as dataMng

#---Threads---#
from ThreadGrabber import ThreadGrabber

#---Settings---#
#IntervalGrabber = 10 # = 10sec
IntervalGrabber = 1 # = 1sec
startDelay = 1
intervalRequest = 0.8
setDB = False

#---Timer Threads---#
threadTimerGrabber = ThreadGrabber(IntervalGrabber, startDelay)

#---Start---#
def main():
	print(sys.argv)
	if len(sys.argv) > 1:
		if sys.argv[1] == 'DataSetMode':
			setDB = True
		elif sys.argv[1] == 'TraderMode':
			setDB = False
		else:
			setDB = True
	else:
		setDB = True
	threadTimerGrabber.start()
	while(True):
		try:
			if setDB == True:
				ask, bid = opl.GetJsonPrices()
				flag = False
				if ask > 0 and bid > 0:
					flag = True
				if flag == True:
					dataMng.setMarketPrice(ask, bid)
					time.sleep(intervalRequest)
		except Exception as e:
			print(e)

if __name__ == '__main__':
	main()

#---END---#