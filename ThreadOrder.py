##!/usr/bin/env python
# -*- coding: utf-8 -*-

#---Packages---#
import socket
import threading
import time
from datetime import datetime
from enum import Enum
import signal

import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.positions as positions
import oandapyV20.endpoints.transactions as trans

#---Library---#
import ArpOandaPy as oanda
import OandaPyLib as opl

class ThreadGrabber():
    def __init__(self, interval, startDelay):
        self.startDelay = startDelay
        self.interval = interval
    
    def task(self, arg, args):
        logger = "ThreadTimerGrabber---{}".format(datetime.now().strftime("%Y/%m/%d %H:%M.%S"))
        timeGetPrice, ask, bid = opl.GetPrices()
        logger = logger + ',' + str(timeGetPrice) + ',' + str(ask) + ',' + str(bid)
        print(logger)

#---END---#