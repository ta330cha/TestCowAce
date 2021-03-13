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
IntervalTrader = 300 # = 600sec = 10min
#IntervalTrader = 60 # = 60sec = 1min
IntervalExecuteRequests = 30
StartDelay = IntervalTrader/100
#startDelay = 1

#---Timer Threads---#
threadTimerTrader = ThreadTrader(IntervalTrader, StartDelay)
threadTimerExecuteRequests = ThreadExecuteRequests(IntervalExecuteRequests, StartDelay + IntervalTrader)

#---Start---#
def main():
	print(sys.argv)
	threadTimerTrader.start()
	threadTimerExecuteRequests.start()
	flag = True
	while(flag):
		time.sleep(IntervalTrader)

if __name__ == '__main__':
	main()

#---END---#