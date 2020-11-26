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
import OandaPyLib as opl

class ThreadTrader():
    def __init__(self, interval, startDelay):
        self.startDelay = startDelay
        self.interval = interval
    
    def task(self, arg, args):
        logger = "ThreadTimerTrader---{}".format(datetime.now().strftime("%Y/%m/%d %H:%M.%S"))
        print(logger)   
    
    def start(self):
        signal.signal(signal.SIGALRM, self.task)
        signal.setitimer(signal.ITIMER_REAL, self.startDelay, self.interval)

#---END---