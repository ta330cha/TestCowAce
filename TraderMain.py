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
#IntervalTrader = 600 # = 600sec = 10min
IntervalTrader = 60 # = 60sec = 1min
startDelay = IntervalTrader
startDelay = 1
intervalRequest = 1

#---File Names---#
OrderTemplatePathname = './Template/OrderTemplate.json'
TransTemplatePathname = './Template/TransTemplate.json'
OrderRequestsDirName = "./OrderRequests/"

#---Timer Threads---#
threadTimerTrader = ThreadTrader(IntervalTrader, startDelay)

#---Start---#
def main():
	print(sys.argv)
	threadTimerTrader.start()
	while(True):
		if opl.RequestOrder() == True:
			time.sleep(intervalRequest)
		if opl.RequestTradeCRCDO() == True:
			time.sleep(intervalRequest)

if __name__ == '__main__':
	main()

#---END---#