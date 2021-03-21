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
from ThreadExecuteRequests import ThreadExecuteRequests

#---Settings---#
IntervalTrader = 10 # = 600sec = 10min
StartDelayTrader = 1
IntervalExecuteRequests = 10
StartDelayExecuteRequests = IntervalTrader + IntervalTrader/2

#---Timer Threads---#
threadTimerTrader = ThreadTrader(IntervalTrader, StartDelayTrader)
threadTimerExecuteRequests = ThreadExecuteRequests(IntervalExecuteRequests, StartDelayExecuteRequests)

#---Start---#
def main():
	print(sys.argv)
	threadTimerTrader.start()
	#threadTimerExecuteRequests.start()
	flag = True
	while(flag):
		time.sleep(IntervalTrader)

if __name__ == '__main__':
	main()

#---END---#