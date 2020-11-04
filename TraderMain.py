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
from ThreadGrabber import ThreadGrabber

#---Settings---#
IntervalTrader = 60 # = 60sec = 1min
IntervalGrabber = 10 # = 10sec
startDelay = 1

#---File Names---#
OrderTemplatePathname = './Template/OrderTemplate.json'
TransTemplatePathname = './Template/TransTemplate.json'
OrderRequestsDirName = "./OrderRequests/"

#---Timer Threads---#
threadTimerTrader = ThreadTrader(IntervalTrader, startDelay)
threadTimerGrabber = ThreadGrabber(IntervalGrabber, startDelay)

#---Start---#
def main():
    threadTimerTrader.start()
    #threadTimerGrabber.start()
    while(True):
        opl.RequestOrder()
        time.sleep(1)

if __name__ == '__main__':
    main()

#---END---#