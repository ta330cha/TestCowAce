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

#---Start---#
def main():
	threadTimerGrabber.start()
	while(True):
		time.sleep(intervalRequest)

if __name__ == '__main__':
	main()

#---END---#