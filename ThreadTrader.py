##!/usr/bin/env python
# -*- coding: utf-8 -*-

#---Packages---#
import socket
import threading
import time
from datetime import datetime
from enum import Enum

#---Library---#
import ArpOandaPy as oanda

class ModeFlag(Enum):
    PublishNewOrder = 1
    EditPosition = 2
    EMS = 666
    Default = 0

class ThreadTrader(threading.Timer):
    def __init__(self, interval):
        self.interval = interval
        self.prevTimeStamp = datetime.now()
        self.nowTimeStamp = datetime.now()
        self.tradeMode = ModeFlag.Default
        self.STOPFLAG = False

    def start(self):
        thread = threading.Thread(target=self.__task)
        thread.start()
    
    def __task(self):
        logger = "ThreadTimer---{}".format(datetime.now().strftime("%Y/%m/%d %H:%M.%S"))
        print(logger)
        
        #---Select Mode---#
        self.tradeMode = __selectMode()
        
        #---Publish New Order---#
        if self.tradeMode == ModeFlag.PublishNewOrder:
            self.__publishNewOrder()
            self.tradeMode = ModeFlag.Default
        
        #---Edit Position---#
        if self.tradeMode == ModeFlag.EditPosition:
            self.__editPosition()
            self.tradeMode = ModeFlag.Default
        
        #---Emergency Stop---#
        if self.tradeMode == ModeFlag.EMS:
            self.STOPFLAG = True
        
        if self.STOPFLAG == False:
            thread = threading.Timer(self.interval, self.__task)
            thread.start()
        else:
            logger = "Emergency---{}".format(datetime.now().strftime("%Y/%m/%d %H:%M.%S"))
            print(logger)

    def __selectMode(self):
        #---From DB, New or Not---
        # Get TimeStamp
        retFlag = ModeFlag.Default
        if self.nowTimeStamp == self.prevTimeStamp:
            retFlag = ModeFlag.EditPosition
        else:
            retFlag = ModeFlag.PublishNewOrder
        
        # Chack EMS or Not
        # retFlag = ModeFlag.EMS

        #---Debug Code---#
        #retFlag = ModeFlag.EditPosition
        #retFlag = ModeFlag.PublishNewOrder
        retFlag = ModeFlag.EMS

        return retFlag

    def __publishNewOrder(self):
        print("Publish new order")
    
    def __editPosition(self):
        print("Edit Position")

#---END---