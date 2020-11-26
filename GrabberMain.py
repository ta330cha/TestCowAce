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
from ThreadGrabber import ThreadGrabber

#---Settings---#
IntervalGrabber = 10 # = 10sec
startDelay = 1
intervalRequest = 1

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