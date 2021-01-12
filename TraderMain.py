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

#---Threads---#
from ThreadTrader import ThreadTrader

#---Settings---#
IntervalTrader = 300 # = 600sec = 10min
#IntervalTrader = 60 # = 60sec = 1min
startDelay = IntervalTrader/100
#startDelay = 1
intervalRequest = 1

#---Timer Threads---#
threadTimerTrader = ThreadTrader(IntervalTrader, startDelay)

#---Start---#
def main():
	print(sys.argv)
	threadTimerTrader.start()
	flag = True
	while(flag):
		if opl.RequestOrder() == True:
			time.sleep(intervalRequest)
		if opl.RequestTradeCRCDO() == True:
			time.sleep(intervalRequest)
		if opl.GetMarginLevel() < opl.MarginLevelLimit:
			flag = True
		else:
			flag = False

if __name__ == '__main__':
	main()

#---END---#