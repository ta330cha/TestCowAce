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
import ArpOandaPy as oanda
import OandaPyLib as opl
from ArpCSVList import ArpCSVList

#---Manager---#
dataMng = ArpCSVList()

class ThreadGrabber():
    def __init__(self, interval, startDelay):
        self.startDelay = startDelay
        self.interval = interval
    
    def task(self, arg, args):
        logger = "ThreadTimerGrabber---{}".format(datetime.now().strftime("%Y/%m/%d %H:%M.%S"))
        timeGetPrice, ask, bid = opl.GetPrices()
        dataMng.setMarketPrice(ask, bid)
        logger = logger + ',' + str(timeGetPrice) + ',' + str(ask) + ',' + str(bid)
        print(logger)
    
    def start(self):
        signal.signal(signal.SIGALRM, self.task)
        signal.setitimer(signal.ITIMER_REAL, self.startDelay, self.interval)

#---END---#