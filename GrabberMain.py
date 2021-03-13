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
from ThreadSetData import ThreadSetData

#---Settings---#
#IntervalGrabber = 10 # = 10sec
IntervalGrabber = 1 # = 1sec
IntervalSetData = 10 # = 10sec
startDelay = 1
intervalRequest = 0.8
setDB = False

#---Timer Threads---#
threadTimerGrabber = ThreadGrabber(IntervalGrabber, startDelay)
threadTimerSetData = ThreadSetData(IntervalSetData, startDelay+IntervalGrabber)

#---Start---#
def main():
	print(sys.argv)
	if len(sys.argv) > 1:
		if sys.argv[1] == 'DataSetMode':
			setDB = True
		elif sys.argv[1] == 'TraderMode' or sys.argv[1] == 'TradeMode':
			setDB = False
		else:
			setDB = True
	else:
		setDB = True
	if setDB == True:
		print("DataSetMode")
	else:
		print("TraderMode")
	threadTimerGrabber.start()
	if setDB == True:
		threadTimerSetData.start()
	while(True):
		time.sleep(intervalRequest)

if __name__ == '__main__':
	main()

#---END---#